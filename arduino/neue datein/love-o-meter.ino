const int sensorPin = A0;
const float baselineTemp = 20.0;

void setup(){
    Serial.begin(9600);
    
    for (int pinNumber = 2; pinNumber < 5; pinNumber++){
        pinMode(pinNumber, OUTPUT);
        digitalWrite(pinNumber, LOW);
    }
}

void loop(){
    int sensorVal = analogRead(sensorPin);
    Serial.print("Sensor Value: ");
    Serial.print(sensorVal);
}