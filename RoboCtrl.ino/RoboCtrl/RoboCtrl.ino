#include <SoftwareSerial.h>
SoftwareSerial BT(3, 5);
String str;
void setup() 
{
  Serial.begin(9600);
  BT.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

char c;

void loop() {
      digitalWrite(6, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
  if(Serial.available()) 
  {
    delay(10);
    c = Serial.read();
    Serial.println("test");
  }
  
  if (c == '1')
  {
    digitalWrite(6, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
    delay(1500);
  }
  else if (c == '2')
  {
    digitalWrite(6, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
    delay(1500);
  }
  else if (c == '3')
  {
    digitalWrite(6, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
    delay(1500);
  }
}


