#include <Wire.h>

#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  125 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  575 // this is the 'maximum' pulse length count (out of 4096)

char data[2];

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  pwm.setPWM(0, 0, angleToPulse(90)); 
  pwm.setPWM(1, 0, angleToPulse(90)); 
  pwm.setPWM(2, 0, angleToPulse(90)); 
  pwm.setPWM(3, 0, angleToPulse(90));
  //yield();
}

// the code inside loop() has been updated by Robojax
void loop() {
  if (Serial.available() > 0) {
    int len = Serial.readBytes(data, 2);
    if (len == 2) {
      int angle_x = data[0];
      int angle_y = data[1];
      //Serial.print("angle x:"); Serial.println(angle_x);
      //Serial.print("angle y:"); Serial.println(angle_y);
      pwm.setPWM(0, 0, angleToPulse(angle_x)); 
      pwm.setPWM(1, 0, angleToPulse(angle_y)); 
      pwm.setPWM(2, 0, angleToPulse(angle_x)); 
      pwm.setPWM(3, 0, angleToPulse(angle_y)); 
    }
  }
}

/*
 * angleToPulse(int ang)
 * gets angle in degree and returns the pulse width
 * also prints the value on seial monitor
 * written by Ahmad Nejrabi for Robojax, Robojax.com
 */
int angleToPulse(int ang){
   return map(ang,0, 180, SERVOMIN,SERVOMAX);// map angle of 0 to 180 to Servo min and Servo max 
}
