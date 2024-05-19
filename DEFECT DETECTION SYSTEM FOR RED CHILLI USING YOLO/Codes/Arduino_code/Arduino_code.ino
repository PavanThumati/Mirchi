
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
    delay(1000);
    Servo1.write(0); 
    delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(180); 
   delay(1000);
  }

}
