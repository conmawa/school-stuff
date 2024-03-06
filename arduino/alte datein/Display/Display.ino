#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
#include <NewPing.h>

const int triggerPin = 12;   
const int echoPin = 11;     
const int maxDistance = 400;

const int redPin = 8;
const int greenPin = 9;
const int bluePin = 10;


void setColourRgb(unsigned int red, unsigned int green, unsigned int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

int lcdi2c = 0x27; // <- Hart eingecodete Adresse, die nur für unser
                   // Beispiel funktioniert, vgl. Datenblatt
                   
NewPing sonar(triggerPin, echoPin, maxDistance);
LiquidCrystal_PCF8574 lcd(lcdi2c);

void setup()
{
  lcd.clear();
  lcd.begin(16, 2);
  lcd.setBacklight(255);
}

void loop()
{
  lcd.setBacklight(255);
  delay(300);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(sonar.ping_cm());
  lcd.setCursor(5,0);
  lcd.print("cm");
  if (sonar.ping_cm() >200){
    setColourRgb(0,255,0);
  }
  if (sonar.ping_cm() >100 and sonar.ping_cm() <200){
    setColourRgb(255,255,0);
  }
  if (sonar.ping_cm() >50 and sonar.ping_cm() <100){
    setColourRgb(255,165,0);
  }
  if (sonar.ping_cm() <50){
    setColourRgb(255,0,0);
  }
 }
