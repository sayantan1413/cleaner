import pyrebase
from time import strftime
from colored import fg


config1 = {
  "apiKey": "apiKey",
  "authDomain": "iot-project-e2f42.firebaseapp.com",
  "databaseURL": "https://iot-project-e2f42.firebaseio.com",
  "storageBucket": "iot-project-e2f42.appspot.com"
}

config2 = {
  "apiKey": "apiKey",
  "authDomain": "iotdevice1-45a7e.firebaseapp.com",
  "databaseURL": "https://iotdevice1-45a7e.firebaseio.com",
  "storageBucket": "iotdevice1-45a7e.appspot.com"
}

firebase = pyrebase.initialize_app(config1)
db1 = firebase.database()

firebase = pyrebase.initialize_app(config2)
db2 = firebase.database()

color = fg('red')
color1 = fg('blue')


print("WELCOME THIS IS AN IOT FIRE ALERT SYSTEM WHERE YOU CAN SEE WHETHER YOU ARE SAFE FROM FIRE OR NOT AND THERE ARE TWO DEVICES ONE AT TAMIL NADU AND OTHER AT WEST BENGAL.")
print("\n")
print("PROJECT AUTHOR : SAYANTAN BOSE")
print("\n")
date = strftime("%m/%d/%Y")
print("Date:", date)
print("\n")
users = db1.child("Device 0 WEST BENGAL").get()
print("DEVICE 0 WEST BENGAL : ",users.val())

users = db2.child("Device 2 TAMIL NADU").get()
print("Device 2 TAMIL NADU : ",users.val())

def stream_handler(message):

    s = message["data"]

    if s == 0:
      print(color + "ALERT !!! THERE IS A FIRE IN DEVICE 0\n")

      time1 = strftime("%H:%M:%S")
      print("Time:", time1)
      print("\n")


    else:
      print(color1 + "CONGO !!! THE FIRE HAS BEEN EXTINGUISED IN DEVICE 0\n")

      time1 = strftime("%H:%M:%S")
      print("Time:", time1)
      print("\n")


my_stream1 = db1.stream(stream_handler)

def stream_handler(message):

    s = message["data"]

    if s == 0:
      print(color + "ALERT !!! THERE IS A FIRE IN DEVICE 2\n")

      time1 = strftime("%H:%M:%S")
      print("Time:", time1)
      print("\n")


    else:
      print(color1 + "CONGO !!! THE FIRE HAS BEEN EXTINGUISED IN DEVICE 2\n")

      time1 = strftime("%H:%M:%S")
      print("Time:", time1)
      print("\n")

my_stream2 = db2.stream(stream_handler)





