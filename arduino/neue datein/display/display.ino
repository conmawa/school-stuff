#include <LiquidCrystal.h>
LiquidCrystal lcd(3, 4, 5, 6, 11, 12);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2); // Initialize LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  Serial.println("What do you want to send to the Arduino?");
}

void loop() {
  if (Serial.available()) {
    lcd.clear(); // Clear the LCD screen
    lcd.setCursor(0,0);
    String message = Serial.readString();
    if (message.length() <= 16) {
      lcd.print(message); // Print received message
    } else {
      // Scroll the text if it exceeds the display width
      for (int i = 0; i <= message.length() - 16; i++) {
        lcd.print(message.substring(i, i + 16));
        delay(500); // Adjust the scrolling speed if needed
      }
    }
  }
}
