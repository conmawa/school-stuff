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
  Serial.println("Geben Sie die Zahlenwerte ein!");
  delay(5000);
  String LEDCommand =Serial.readString();
  Serial.print("Zerlege das Befehlswort: ");
  
  
  Serial.println(LEDCommand);

  int  LEDValues [] = {0,0,0};
  int startPosition = 0;
  for (int i=0; i<3; i++){
    int CommaPosition = LEDCommand.indexOf(",");
    String colorString = LEDCommand.substring(startPosition, CommaPosition);
    int colorStringLength = colorString.length();
    LEDValues[i] = colorString.toInt();

    LEDCommand.remove(startPosition, colorStringLength + 1);
    LEDCommand.trim();
  }
  
  Serial.println(LEDValues[0]);
  Serial.println(LEDValues[1]);
  Serial.println(LEDValues[2]);
  int LED1=LEDValues[0];
  int LED2=LEDValues[1];
  int LED3=LEDValues[2];
  setColourRgb(LED1, LED2, LED3);
}

void loop() {
  
}
