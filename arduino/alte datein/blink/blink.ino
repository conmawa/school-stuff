const int ledPin = 13;
const int frq = 500;
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  Serial.println("an");
  delay(frq);
  digitalWrite(ledPin, LOW);
  Serial.println("aus");
  delay(frq);
}
