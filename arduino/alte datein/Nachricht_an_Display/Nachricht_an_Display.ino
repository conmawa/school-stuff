#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>

int lcdi2c = 0x27; // <- Hart eingecodete Adresse, die nur für unser
                   // Beispiel funktioniert, vgl. Datenblatt

void setup()
{
  Serial.begin(9600);
  Serial.println("Bitte Nachricht eingeben:");
  LiquidCrystal_PCF8574 lcd(lcdi2c);
  lcd.cursor();
  lcd.blink();
  lcd.autoscroll();
  lcd.leftToRight();
  lcd.begin(16, 2);
  lcd.setBacklight(255);
  delay(5000);
  String Nachricht=Serial.readString();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(Nachricht);
}

void loop()
{
  
}
