#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(12, 13); // RX, TX
LiquidCrystal lcd(3, 4, 5, 6, 10, 11);

int screenWidth = 16;
int screenHeight = 2;
String line1 = "Message:";
String line2 = "";

int stringStart = 0;
int stringEnd = 0;
int scrollCursor = screenWidth;
int green = 8;
int red = 9;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  lcd.begin(screenWidth, screenHeight);
  Serial.println("Whats your Message?");
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  digitalWrite(red, HIGH);
  delay(1000);
}

void loop() {
  lcd.setCursor(3, 0);
  lcd.print(line1);

  if (Serial.available()) {
    String outgoingMessage = Serial.readStringUntil('\n');
    Serial.println("Sending message: " + outgoingMessage);
    mySerial.println(outgoingMessage);
  }else{
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
  }

  while (mySerial.available()) {
    String receivedString = mySerial.readStringUntil('\n'); 
    Serial.println("Received message: " + receivedString);
    digitalWrite(green, LOW);
    digitalWrite(red, HIGH);
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