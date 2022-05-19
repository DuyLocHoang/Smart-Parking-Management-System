import cv2
import numpy as np
import logging
from drawing_utils import draw_contours
from colors import COLOR_GREEN, COLOR_WHITE, COLOR_BLUE
import time
from shapely.geometry import box
from shapely.geometry import Polygon as shapely_poly
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
class MotionDetector:

    def __init__(self, video, coordinates,weight_dir,config_dir,class_dir):
        self.video = video
        self.coordinates_data = coordinates
        # self.start_frame = start_frame
        self.contours = []
        self.bounds = []
        self.mask = []
        self.weight_dir = weight_dir
        self.config_dir = config_dir
        self.class_dir = class_dir
        self.parked = {}
        self.FPS = 1
    def get_car_boxes(self,boxes, class_ids):
        car_boxes = []

        for i, box in enumerate(boxes):
            # If the detected object isn't a car / truck, skip it
            if class_ids[i] in [2]:
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


    def predict(self,img,net,output_layers):
        height, width, channels = img.shape

        with open(self.class_dir, 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        blob = cv2.dnn.blobFromImage(img, 0.00392, (320,320), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

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

    def detect_motion(self):
        start_time = time.time()
        display_time = 2
        fps = 0
        cTime = 0
        pTime = 0
        # Load yolov3-tiny weight and config
        net = cv2.dnn.readNet(self.config_dir, self.weight_dir)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        # net2 = cv2.dnn.readNet("cfg/yolov3.cfg","weights/yolov3.weights")
        # net2.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # net2.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        # layer_names2 = net2.getLayerNames()
        # output_layers2 = [layer_names2[i - 1] for i in net2.getUnconnectedOutLayers()]


        capture = cv2.VideoCapture("http://192.168.1.7:8080", apiPreference=cv2.CAP_FFMPEG)
        fps_real = capture.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps_real))
        # capture.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)

        coordinates_data = self.coordinates_data
        parked = self.parked
        id = []
        for p in coordinates_data:
            coordinates = self._coordinates(p)
            id.append(self._id(p))
            self.contours.append(coordinates)
        parked["id"] = id
        # print(parked["id"])
        parked["coordinates"] = self.contours
        # print(parked["coordinates"][0])
        counts = 0
        while capture.isOpened():
            result, frame = capture.read()
            overlay = frame.copy()
            counts +=1
            if frame is None:
                break

            if not result:
                raise CaptureReadError("Error reading video capture on frame %s" % str(frame))

            process_frame = 2

            if counts%2 == 0 :

                frame,car_boxes = self.predict(frame,net,output_layers)
                overlaps = self.compute_overlaps(parked["coordinates"],car_boxes)
                # print(overlaps)
                state = {}
                for parking_area, overlap_areas, id in zip(parked["coordinates"],overlaps,parked["id"]):
                    max_IoU_overlap = np.max(overlap_areas)
                    car_id = np.argmax(overlap_areas)
                    # print(car_boxes[car_id])
                    # print(parking_area[0][0])
                    cv2.putText(frame,str(id),(parking_area[0][0],parking_area[0][1]),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),3)
                    if max_IoU_overlap < 0.15:
                        cv2.fillPoly(frame, [np.array(parking_area)], (71, 27, 92))
                        free_space = True
                        state[str(id)] = True

                    else:
                        state[str(id)] =False
                        # cv2.rectangle(frame, (car_boxes[car_id][0], car_boxes[car_id][1]), (
                        # car_boxes[car_id][0] + car_boxes[car_id][2], car_boxes[car_id][1] + car_boxes[car_id][3]),
                        #               (0, 255, 0), -1)
                        # # print(car_id)
                        # roi = overlay[car_boxes[car_id][1]:car_boxes[car_id][1] + car_boxes[car_id][3],car_boxes[car_id][0]: car_boxes[car_id][0] + car_boxes[car_id][2]]
                        # cv2.imshow("roi",roi)
                        # # print(roi.shape)
                        # predict_roi, car_plate_location = self.predict(roi, net, output_layers)
                        # # cv2.imshow("Duyloc",predict_roi)
                        # # # print("cccc")
                        # # x_plate,y_plate,w_plate,h_plate = car_plate_location
                        # # roi_plate = roi[y_plate:y_plate + h_plate,x_plate: x_plate + w_plate]
                        # # print(predict_roi.shape)
                        # txt = pytesseract.image_to_string(predict_roi)
                        # # print("{}: {}".format(id,txt))
                        # # print(car_plate.shape)

                # print(state)
                cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
                fps +=2
                TIME = time.time() - start_time

                if TIME > display_time :
                    print("FPS", round(fps/TIME))
                    fps = 0
                    start_time = time.time()

                # cTime = time.time()
                # self.FPS = process_frame/(cTime-pTime)
                # pTime = cTime
                # cv2.putText(frame,str(int(self.FPS)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),5)
                cv2.imshow(str(self.video), frame)

            if cv2.waitKey(7) & 0xff == ord("q"):
                break
        capture.release()
        cv2.destroyAllWindows()


    @staticmethod
    def _coordinates(p):
        return np.array(p["coordinates"])

    @staticmethod
    def _id(p):
        return np.array(p["id"])




class CaptureReadError(Exception):
    pass


# import cv2
# import time
#
# if __name__ == '__main__' :
#
#     # Start default camera
#     video = cv2.VideoCapture("D:\LVTN\combine\\videos\parking_lot_1.mp4")
#     while True :
#         success,img = video.read()
#         cv2.imshow("FPS",img)
#         if cv2.waitKey(40) & 0xff == ord("q"):
#             break
#     # Find OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#
#     # With webcam get(CV_CAP_PROP_FPS) does not work.
#     # Let's see for ourselves.
#
#     if int(major_ver)  < 3 :
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#     else :
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
#
#     # Number of frames to capture
#     num_frames = 120;
#
#     print("Capturing {0} frames".format(num_frames))
#
#     # Start time
#     start = time.time()
#
#     # Grab a few frames
#     for i in range(0, num_frames) :
#         ret, frame = video.read()
#
#     # End time
#     end = time.time()
#
#     # Time elapsed
#     seconds = end - start
#     print ("Time taken : {0} seconds".format(seconds))
#
#     # Calculate frames per second
#     fps  = num_frames / seconds
#     print("Estimated frames per second : {0}".format(fps))
#     # Release video
#     video.release()