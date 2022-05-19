import pyrebase
import threading
class Sensor:
    def __init__(self):
        self.parkingStatus = None
        self.running = True
        self.running_thread = True
        self.firebaseConfig  = {
              "apiKey": "AIzaSyBHAtb-Ft8n7tuWbj9o2Xx_v_IMEG3uR9w",
              "authDomain": "esp8266-96638.firebaseapp.com",
              "databaseURL": "https://esp8266-96638-default-rtdb.firebaseio.com",
              "projectId": "esp8266-96638",
              "storageBucket": "esp8266-96638.appspot.com",
              "messagingSenderId": "492800014336",
              "appId": "1:492800014336:web:5c8daea4da5862bd8100e5",
              "measurementId": "G-91RWXND4J0"
            };
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)

        self.db = self.firebase.database()
        self.thread = threading.Thread(target=self.update_data)
        self.thread.start()
    def update_data(self):
        while self.running_thread:
            if self.running:
                dataFromFirebase = self.db.get()
                status = dataFromFirebase.val()
                pre_status = status.get('data')
                if pre_status == 0 :
                    self.parkingStatus = "Free"
                else :
                    self.parkingStatus = "Busy"

                # print("aaaa")

    def __del__(self):
        if self.running:
            self.running_thread = False
            self.running = False
            self.thread.join()

if __name__ == "__main__":
    Sensor()