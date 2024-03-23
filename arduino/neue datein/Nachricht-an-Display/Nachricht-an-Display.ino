  #include <LiquidCrystal.h>
  LiquidCrystal lcd(3, 4, 5, 6, 11, 12);

  int screenWidth = 16;
  int screenHeight = 2;
  String line1 = "Message:";
  String line2 = "";

  int stringStart = 0;
  int stringEnd = 0;
  int scrollCursor = screenWidth;

  void setup() {
    Serial.begin(9600);
    lcd.begin(screenWidth, screenHeight);
  }

  void loop() {
    lcd.setCursor(3, 0);
    lcd.print(line1);

    while (Serial.available()) {
      String receivedString = Serial.readString(); // Read the incoming byte

      // Append the received character to line2
      if (receivedString != '\n' && receivedString != '\r') {
        line2 = "";
        line2 += receivedString;
        scrollCursor = screenWidth;
        stringStart = 0;
        stringEnd = 0;
        lcd.clear();
      }
    }

    lcd.setCursor(scrollCursor, 1);
    lcd.print(line2.substring(stringStart, stringEnd));
    delay(500);
    lcd.clear();

    if (stringStart == 0 && scrollCursor > 0){
      scrollCursor --;
      stringEnd ++;
    } else if (stringStart == stringEnd){
      stringStart = stringEnd = 0;
      scrollCursor = screenWidth;
    } else if(stringEnd == line2.length() && scrollCursor == 0){
      stringStart ++;
    } else{
      stringStart ++;
      stringEnd ++;
    }

  }