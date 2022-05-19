import cv2
import PIL.Image
import time
import threading
import numpy as np
from utils.path_direct import *
from utils.yolo import *
import os
from shapely.geometry import Polygon as shapely_poly
import yaml
from datetime import datetime
import requests
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"


class Camera:
    def __init__(self, model, src=0,data_file = None,location = None):

        self.model = model
        self.src = src
        self.fps = None
        self.location = location
        self.yolo_confident = 0.5
        self.yolo_iou = 0.5
        self.total = 0
        self.free = 0
        #---------------------------------------
        self.data_file = data_file

        self.contours = []
        self.bounds = []
        self.mask = []
        self.parked = {}
        id = []
        contours = []

        with open(data_file, "r") as data:
            points = yaml.safe_load(data)

            for p in points :
                contours.append(np.array(p["coordinates"]))
                id.append(np.array(p["id"]))
        self.parked["id"] = id
        self.parked["coordinates"] = contours

        #------------------------------
        self.data_push = []

        #-------------------------------
        # Flag
        self.flagErr = False

        # default value for video
        self.ret = False
        self.frame = None
        self.vid = None
        self.image_save = None
        self.convert_color = cv2.COLOR_BGR2RGB
        self.convert_pillow = True
        self.running = True

        # Open the video source
        if self.src == '0':
            self.src = 0
        try:
            if self.src == 0:
                self.vid = cv2.VideoCapture(self.src, cv2.CAP_DSHOW)
            else:
                self.vid = cv2.VideoCapture(self.src, apiPreference=cv2.CAP_FFMPEG)
            if not self.fps:
                self.fps = int(self.vid.get(cv2.CAP_PROP_FPS))
                if self.fps == 0:
                    self.fps = 25
            if not self.vid.isOpened():
                self.running = False
        except:
            self.running = False
            print('err')
        # Load net and blob and area using for processing image
        self.net = None
        if self.net == None:
            if self.model == 'yolov3':
                self.net = cv2.dnn.readNet(MODEL_YOLOV3, CONFIG_YOLOV3)

            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.blob = None
        self.area = None


        # Create Thread and run
        self.running_thread = True
        self.thread = threading.Thread(target=self.yolov3)
        self.thread2 = threading.Thread(target=self.backend)
        self.thread.start()
        self.thread2.start()

    def backend(self):
        # while self.running_thread:
        #     if self.running:
        #         r = requests.post("http://localhost:8080/data", json=self.data_push)
        #             # print(r.text)
        print("thread2")


    # def insert_statedb(self,state, slotID):
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="duyloc",
    #         database="parking"
    #
    #     )
    #     mycursor = mydb.cursor()
    #
    #     Q1 = "INSERT INTO states (time, state, slotID) VALUES (%s,%s,%s)"
    #     val = (datetime.now(), state, slotID)
    #
    #     mycursor.execute(Q1, val)
    #     mydb.commit()
    #     print(mycursor.rowcount, "state data inserted.")

    def get_car_boxes(self,boxes, class_ids):
        car_boxes = []

        for i, box in enumerate(boxes):
            # If the detected object isn't a car / truck, skip it
            if class_ids[i] in [2,5,7]:
                car_boxes.append(box)

        return np.array(car_boxes)

    def compute_overlaps(self,parked_car_boxes, car_boxes):
        new_car_boxes = []
        for box in car_boxes:
            y1 = box[1]
            x1 = box[0]
            y2 = box[1]+box[3]
            x2 = box[0]+box[2]

            p1 = (x1, y1)
            p2 = (x2, y1)
            p3 = (x2, y2)
            p4 = (x1, y2)
            new_car_boxes.append([p1, p2, p3, p4])

        overlaps = np.zeros((len(parked_car_boxes), len(new_car_boxes)))
        for i in range(len(parked_car_boxes)):
            for j in range(car_boxes.shape[0]):
                pol1_xy = parked_car_boxes[i]
                pol2_xy = new_car_boxes[j]
                polygon1_shape = shapely_poly(pol1_xy)
                polygon2_shape = shapely_poly(pol2_xy)

                polygon_intersection = polygon1_shape.intersection(polygon2_shape).area
                polygon_union = polygon1_shape.union(polygon2_shape).area
                IOU = polygon_intersection / polygon_union
                overlaps[i][j] = IOU

        return overlaps

    def predict(self,img):
        height, width, channels = img.shape

        with open(LABEL_NAME, 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        self.blob = cv2.dnn.blobFromImage(img, 0.00392, (320,320), (0, 0, 0), True, crop=False)
        self.net.setInput(self.blob)
        outs = self.net.forward(get_output_layers(self.net))

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected

                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)


                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    # cv2.circle(img,(x,y),5,(0,255,255),-1)
                    boxes.append([x, y, w, h])
                    # print(boxes)
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        # print(boxes)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        car_boxes = self.get_car_boxes(boxes, class_ids)

        for i in range(len(boxes)):
            if i in indexes:
                if class_ids[i] in [2,5,7]:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    color = (0,255,0)
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
                    font = cv2.FONT_HERSHEY_PLAIN
                    cv2.putText(img, label, (x, y), font, 0.5, color, 1)
        return img,car_boxes


    # Main process
    def yolov3(self):
        start = time.time()
        startx = time.time()
        end = 0
        count = 0

        # fps = 0
        # cTime = time.time()
        # pTime = 0
        while self.running_thread:
            if self.running:
                try:
                    ready_data = []
                    ret, frame = self.vid.read()
                    overlay = frame.copy()
                    Width = frame.shape[1]
                    Height = frame.shape[0]
                    frame = cv2.resize(frame, (Width, Height))
                    c = 0
                    count += 1
                    if ret and count % 4 == 0:
                        frame, car_boxes = self.predict(frame)
                        overlaps = self.compute_overlaps(self.parked["coordinates"], car_boxes)
                        state = {}
                        for parking_area, overlap_areas, id in zip(self.parked["coordinates"], overlaps, self.parked["id"]):
                            max_IoU_overlap = np.max(overlap_areas)
                            car_id = np.argmax(overlap_areas)
                            cv2.putText(frame, str(id), (parking_area[0][0], parking_area[0][1]),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 3)
                            if max_IoU_overlap < 0.15:
                                cv2.fillPoly(frame, [np.array(parking_area)], (71, 27, 92))
                                state[str(id)] = True
                            else:
                                state[str(id)] = False

                            res_status = 0
                            if state[str(id)]:
                                res_status = 1
                            ready_data.append({"name": self.location +"-"+ str(id), "location": self.location, "status": bool(state[str(id)]),'reserve_status': bool(res_status)})
                            if len(ready_data) == len(self.parked["coordinates"]) :
                                self.data_push = ready_data
                                # print(ready_data)
                        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
                        self.total = len(state)
                        for f in state.values() :
                            if f == True :
                                c +=1
                        self.free = c
                        # print(self.total)
                        # print(self.free)
                        print("FPS",int(4/(time.time()-startx)))
                        startx = time.time()

                        Put_time_date_FPS(frame, count, start,self.fps)

                        self.img_show = frame
                except:
                    pass

                # Update frame
                self.ret = ret
                self.frame = frame

    def get_frame(self):
        return self.ret, self.frame

    def __del__(self):
        # stop thread
        if self.running:
            self.running_thread = False
            self.running = False
            self.thread.join()
            self.thread2.join()
        # Stop stream
        if self.vid.isOpened():
            self.vid.release()
