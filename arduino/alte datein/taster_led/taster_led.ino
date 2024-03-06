const int buttonPin = 2;     // Pin des Buttons
const int ledPin =  13;      // Pin der LED
int zeit=1000;

// variables will change:
int buttonState = 0;         // Variable für die Speicherung

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
    delay(zeit);
  }
  else {
    digitalWrite(ledPin, LOW);
  }
}
