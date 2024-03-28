#include <SoftwareSerial.h>

SoftwareSerial mySerial(0, 1); // RX, TX

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  if (mySerial.available()) {
    String incomingMessage = mySerial.readStringUntil('\n');
    Serial.println("Received message: " + incomingMessage);
    Serial.println("Please enter a response:");
  }

  if (Serial.available()) {
    String outgoingMessage = Serial.readStringUntil('\n');
    Serial.println("Sending message: " + outgoingMessage);
    mySerial.println(outgoingMessage);
  }
}
