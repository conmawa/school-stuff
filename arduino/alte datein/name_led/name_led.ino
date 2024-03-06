//char incomingByte;
String receivedString;
const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;


void setColourRgb(unsigned int red, unsigned int green, unsigned int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
  
void setup() {
  Serial.begin(9600);
  setColourRgb(0,0,0);
  Serial.println("Geben Sie Ihren Namen ein!");
  
}

void loop() {
  if (Serial.available() > 0) {
        //incomingByte = Serial.read();    // Lesen eines Zeichens
        receivedString = Serial.readString();
        Serial.print(receivedString);
        if (receivedString.equals("constantin")){
           setColourRgb(255, 100, 20);
        }
        if (receivedString.equals("josefa")){
          setColourRgb(20,100,255);
        }
    }
}
