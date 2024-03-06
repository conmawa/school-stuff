char incomingByte;
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
        incomingByte = Serial.read();
        Serial.write(incomingByte);
        if (incomingByte == 'A'){
          Serial.write("A gelesen");
          digitalWrite(ledPin, HIGH);
          delay(3000);
          digitalWrite(ledPin, LOW);
        }
        if (incomingByte == 'B'){
          Serial.write("B gelesen");
          digitalWrite(ledPin, LOW);
        }
    }
}
