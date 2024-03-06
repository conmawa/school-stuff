#include <NewPing.h>
const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;

void setColourRgb(unsigned int red, unsigned int green, unsigned int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
const int triggerPin = 3;   
const int echoPin = 2;     
const int maxDistance = 400;


NewPing sonar(triggerPin, echoPin, maxDistance);

void setup() {
  Serial.begin(9600);
  setColourRgb(0,0,0);
}

void loop() {
  int distanz=sonar.ping_cm();
  Serial.println(sonar.ping_cm());
  if (distanz<20){
    setColourRgb(0,0,0);
    setColourRgb(255,0,0);
  }
  if (distanz<50 and distanz>20){
    setColourRgb(0,0,0);
    setColourRgb(0,255,0);
  }
  if (distanz>100){
    setColourRgb(0,0,0);
    setColourRgb(0,0,255);
  }
}
