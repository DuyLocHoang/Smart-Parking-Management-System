import pyrebase
import numpy as np
firebaseConfig = {
  "apiKey": "AIzaSyCBFmLLI6D4ZVEc8XfYMGPPkadhnu6X03w",
  "authDomain": "test-connect-5041c.firebaseapp.com",
  "databaseURL": "https://test-connect-5041c-default-rtdb.firebaseio.com",
  "projectId": "test-connect-5041c",
  "storageBucket": "test-connect-5041c.appspot.com",
  "messagingSenderId": "297377374112",
  "appId": "1:297377374112:web:5e3866f368712ccb3b8ec5",
  "measurementId": "G-MDMBQYWX1S"
};

# firebaseConfig = {
#   "apiKey": "AIzaSyBHAtb-Ft8n7tuWbj9o2Xx_v_IMEG3uR9w",
#   "authDomain": "esp8266-96638.firebaseapp.com",
#   "databaseURL": "https://esp8266-96638-default-rtdb.firebaseio.com",
#   "projectId": "esp8266-96638",
#   "storageBucket": "esp8266-96638.appspot.com",
#   "messagingSenderId": "492800014336",
#   "appId": "1:492800014336:web:5c8daea4da5862bd8100e5",
#   "measurementId": "G-91RWXND4J0"
# };


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Push data to firebase database

# data = {
#     "Age": 21,
#     "Name": "DuyLoc",
#     "Graduation": True
# }
# for i in range(10):
#     db.child("Users{}".format(i)).set(data)
#     print(i)

# Read data from firebase

dataFromFirebase = db.get()
parkingStatus = dataFromFirebase.val()
# print(parkingStatus)
print(parkingStatus.get('data'))
# print(.val())
# for user in parkingStatus.each():
