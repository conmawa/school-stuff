#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);


void setup() {
  Serial.begin(9600);
  lcd.cursor();
  lcd.begin(16,2);
  Serial.print("What do you want to send to the arduino?");
}


void loop() {
  lcd.blink();
  lcd.clear();

  String input = Serial.readString();
  Serial.println(input);
  lcd.setCursor(0, 0);
  lcd.autoscroll();
  for (int i = 0; i < input.length(); i++) {
    lcd.print(input[i]);
    delay(150);
  }
  
  lcd.noAutoscroll();
}
