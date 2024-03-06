const int ledPin=13;

void setup(){
  pinMode(ledPin, OUTPUT);

    for (int i=0;i<3;i++){
    digitalWrite(ledPin, HIGH);
    delay(400);
    digitalWrite(ledPin, LOW);
    delay(400);
  }
  for(int i=0; i<3; i++){
    digitalWrite(ledPin, HIGH);
    delay(800);
    digitalWrite(ledPin, LOW);
    delay(800);
  }
  for (int i=0;i<3;i++){
    digitalWrite(ledPin, HIGH);
    delay(400);
    digitalWrite(ledPin, LOW);
    delay(400);
  }
}

void loop(){
}
