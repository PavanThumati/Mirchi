import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import cvzone

from cvzone.SerialModule import SerialObject
arduino = SerialObject('COM3')


# Load YOLO model
model = YOLO('best.pt')

# Read class names from coco.txt
with open("Class_Labels1.txt", "r") as file:
    class_list = file.read().split("\n")

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for your primary camera, 1 for secondary, etc.

while True:
    ret, im = camera.read()
    
    if not ret:
        print("Failed to capture image")
        break

    im = cv2.flip(im, 1)
    results = model.predict(im)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]

        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(im, f'{c}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        if int(c)>1:
            arduino.sendData([0])
        else:
            arduino.sendData([1])

    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()



"""
#include <cvzone.h>

SerialData serialData(2, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() {
  pinMode(13, OUTPUT);
  serialData.begin();
}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(13, valsRec[0]);
  delay(10);
}




#include <cvzone.h>


#include <Servo.h> 
// Declare the Servo pin 
int servoPin = 3; 
// Create a servo object 
Servo Servo1; 

SerialData serialData(2, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() {
  
  serialData.begin();
  Servo1.attach(servoPin); 
}

void loop() {

  serialData.Get(valsRec);
  if(valsRec[0]==1){
    Servo1.write(0); 
   delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(90); 
   delay(1000); 
   // Make servo go to 180 degrees 
   Servo1.write(180); 
   delay(1000);
  }

}



"""