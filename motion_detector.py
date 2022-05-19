import cv2 
import numpy as np
import logging
from drawing_utils import draw_contours
from colors import COLOR_GREEN, COLOR_WHITE, COLOR_BLUE
import pandas as pd
import time
import json
import requests
import urllib3
import hmac
import hashlib
import binascii
from register_new_pi import get_keys
import requests
import threading
import time
class MotionDetector:
    LAPLACIAN = 1.5
    DETECT_DELAY = 5
    url = 'http://localhost:8080/data'
    def __init__(self, video, coordinates, start_frame):
        self.video = video
        self.coordinates_data = coordinates
        self.start_frame = start_frame
        self.contours = []
        self.bounds = []
        self.mask = []
        self.threads = []
        self.ready_data = []
        # self.running = True
        # self.running_thread = True
        # self.thread1 = threading.Thread(target=self.backend)
        # self.thread2 = threading.Thread(target=self.testthread2)
        # self.thread1.start()
        # self.thread2.start()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def testthread2(self):

        print("Thread2")

    def backend(self):
        while self.running_thread:
            if self.running:
                correct_payload = [{'username': 'hello'}, {'username': 'hello'}]
                wrong_payload = {'username': 'hello'}
                r = requests.post(MotionDetector.url, json=self.ready_data)
                print(r.text)
        # print('thread1')

    def detect_motion(self):
        start_time = time.time()
        display_time = 2
        fps = 0

        capture = cv2.VideoCapture(self.video)
        capture.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)

        coordinates_data = self.coordinates_data
        logging.debug("coordinates data: %s", coordinates_data)

        for p in coordinates_data:
            # print("p",p)
            #dictionary to array
            coordinates = self._coordinates(p)
            logging.debug("coordinates: %s", coordinates)
            # print('coordinates',coordinates)
            rect = cv2.boundingRect(coordinates)

            self.x, self.y, self.w, self.h = cv2.boundingRect(coordinates)
            # logging.debug("rect: %s", rect)
            # print('rect',rect)
            new_coordinates = coordinates.copy()
            new_coordinates[:, 0] = coordinates[:, 0] - rect[0]
            new_coordinates[:, 1] = coordinates[:, 1] - rect[1]
            # print("new_cor",new_coordinates)

            logging.debug("new_coordinates: %s", new_coordinates)
            # print('new_coordinates',new_coordinates)
            self.contours.append(coordinates)
            self.bounds.append(rect)

            mask = cv2.drawContours(
                np.zeros((rect[3], rect[2]), dtype=np.uint8),
                [new_coordinates],
                contourIdx=-1,
                color=255,
                thickness=-1,
                lineType=cv2.LINE_8)
            cv2.imshow("mask",mask)
            # print("mask",mask)
            mask = mask == 255
            self.mask.append(mask)
            # print(self.mask)
            # cv2.imshow("self.mask",mask)
            # logging.debug("mask: %s", self.mask)
            # print('mask',mask)
        statuses = [False] * len(coordinates_data)
        times = [None] * len(coordinates_data)

        counts = 0
        while capture.isOpened():
            ready_data = []
            result, frame = capture.read()

            counts +=1
            if frame is None:
                break

            if not result:
                raise CaptureReadError("Error reading video capture on frame %s" % str(frame))


            # cv2.imshow("Blur",blurred)
            blurred = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
            grayed = cv2.GaussianBlur(blurred, (5, 5), 1)
            cv2.imshow("Anh Xam",blurred)
            cv2.imshow("Blurred",grayed)
            new_frame = frame.copy()
            logging.debug("new_frame: %s", new_frame)

            position_in_seconds = capture.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
            # print(position_in_seconds)


            for index, c in enumerate(coordinates_data):
                # print(times[index])
                status = self.__apply(grayed, index, c)

                if times[index] is not None and self.same_status(statuses, index, status):
                    times[index] = None
                    continue

                if times[index] is not None and self.status_changed(statuses, index, status):
                    # print(position_in_seconds - times[index])
                    if position_in_seconds - times[index] >= MotionDetector.DETECT_DELAY:
                        statuses[index] = status
                        times[index] = None
                    continue

                if times[index] is None and self.status_changed(statuses, index, status):
                    times[index] = position_in_seconds

                # res_status = 0
                # if status:
                #     res_status = 1
                # ready_data.append(
                #     {"name": 'L' + str(index + 1), "location": "Library", "status": bool(status),
                #      'reserve_status': bool(res_status)})
                # if len(ready_data) == len(coordinates_data) :
                #     self.ready_data = ready_data
                #     print(self.ready_data)
            # print(ready_data)
                # if status:
                #     print(index + 1)
                # print(ready_data)
            ##########################
            # push data to the server
            ##########################

            # pi_id = 123456 # 123456 is a test 'pi'
            # print("pushing data to server")
            # # print(pi_id)
            # keys = get_keys(pi_id)
            # # print(keys)
            # # print(keys.privateKey)
            # # print(type(json.dumps(np.array(keys.privateKey.data, dtype=bool).tolist())))
            # encoded_data = json.dumps(np.array(statuses, dtype=bool).tolist()).encode()
            # # print("array: " + json.dumps(np.array(statuses, dtype=bool).tolist()))
            # signature = hmac.new(key= json.dumps(np.array(keys.privateKey, dtype=bool).tolist()).encode(), msg= encoded_data, digestmod="sha1")
            #
            # data = {
            #     "sign" : signature,
            #     "text" : encoded_data.decode()
            # }
            #
            # req = requests.post('http://localhost:8080/data/{0}'.format(pi_id), data = data)
            # print("done")
            # print(ready_data)
            # correct_payload = [{'username': 'hello'},{'username': 'hello'}]
            # wrong_payload = {'username': 'hello'}
            # r = requests.post(MotionDetector.url, json=correct_payload)
            # print(r.text)
            # r = requests.post(MotionDetector.url, data = json.dumps(ready_data).encode())
            # print(r.text)
            # print(ready_data)
            # if counts%40 == 0:
            #     correct_payload = json.dumps(ready_data).encode('utf-8')
            #     # print(correct_payload)
            #     http = urllib3.PoolManager()
            #     r = http.request('POST', MotionDetector.url, headers={'Content-Type': 'application/json'}, body=correct_payload)

            for index, p in enumerate(coordinates_data):
                coordinates = self._coordinates(p)

                color = COLOR_GREEN if statuses[index] else COLOR_BLUE
                draw_contours(new_frame, coordinates, str(p["id"] + 1), COLOR_WHITE, color)

            # new_frame = cv2.rectangle(new_frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2)
            # cv2.imshow("test",img_test)
            cv2.imshow(str(self.video), new_frame)
            fps +=1
            TIME = time.time() - start_time
            if TIME > display_time :
                # print("FPS", fps/TIME)
                fps = 0
                start_time = time.time()
            k = cv2.waitKey(1)
            if k == ord("q"):
                # if self.running:
                #     self.running_thread = False
                #     self.running = False
                #     self.threads.append(self.thread1)
                #     self.threads.append(self.thread2)
                #     for t in self.threads:
                #         t.join()
                break
        capture.release()
        cv2.destroyAllWindows()

    def __apply(self, grayed, index, p):
        coordinates = self._coordinates(p)
        logging.debug("points: %s", coordinates)

        rect = self.bounds[index]
        logging.debug("rect: %s", rect)
        #lay anh [y,x]
        roi_gray = grayed[rect[1]:(rect[1] + rect[3]), rect[0]:(rect[0] + rect[2])]
        cv2.imshow('roi_gray',roi_gray)
        laplacian = cv2.Laplacian(roi_gray, cv2.CV_64F)
        # laplacian = cv2.Canny(roi_gray, 100,200)
        # cv2.imshow("Canny",canny)
        # print("laplacian: ",np.mean(np.abs(laplacian)))
        # print(laplacian.shape)
        cv2.imshow('Laplacian',laplacian)
        # logging.debug("laplacian: %s", laplacian)
        # print(laplacian)

        coordinates[:, 0] = coordinates[:, 0] - rect[0]
        coordinates[:, 1] = coordinates[:, 1] - rect[1]

        status = np.mean(np.abs(laplacian * self.mask[index])) < MotionDetector.LAPLACIAN
        # logging.debug("status: %s", status)
        print(np.mean(np.abs(laplacian * self.mask[index])))
        return status

    @staticmethod
    def _coordinates(p):
        return np.array(p["coordinates"])

    @staticmethod
    def same_status(coordinates_status, index, status):
        return status == coordinates_status[index]

    @staticmethod
    def status_changed(coordinates_status, index, status):
        return status != coordinates_status[index]

    # def __del__(self):
    #     # stop thread
    #     if self.running:
    #         self.running_thread = False
    #         self.running = False
    #         self.thread.join()

class CaptureReadError(Exception):
    pass

