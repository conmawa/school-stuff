//Bibliotheken einfügen
#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
#include <NewPing.h>

//Distanzmesser: Pins festlegen
const int triggerPin = 12;   
const int echoPin = 11;     
const int maxDistance = 400;

//RGB-LED: Pins festlegen
const int redPin = 8;
const int greenPin = 9;
const int bluePin = 10;

//Grundeinstellungen für die RGB-LED
void setColourRgb(unsigned int red, unsigned int green, unsigned int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

//Display-Konfiguration
int lcdi2c = 0x27; 

//Objekt für Display und Distanzmesser festlegen
NewPing sonar(triggerPin, echoPin, maxDistance);
LiquidCrystal_PCF8574 lcd(lcdi2c);


//Hier ist das was nur einmal ausgeführt wird
void setup()
{
  lcd.clear();
  lcd.begin(16, 2);
  lcd.setBacklight(255);
}

//In diesem Block werden alle Befehlen hinterienander und unendlich oft ausgeführt
void loop()
{
  delay(300);
  lcd.clear();
  //Cursor-Position und anzuzeigender Text festlegen
  lcd.setCursor(0, 0);
  lcd.print("Distanz:");
  lcd.setCursor(2, 1);
  lcd.print(sonar.ping_cm()); //Ist das Objekt des Distanzmessers, indem die Werte gespeichert werden
  lcd.setCursor(5,1);
  lcd.print("cm");
  if (sonar.ping_cm() >200){ //Funktion für die RGB-LED
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
