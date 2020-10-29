#include <EEPROM.h>
int RamPos = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

}

void serialEvent() {
RamPos = 0;
  
  if(Serial.available()) { //메모리 입력 구문
    while (Serial.available()) {
      int c = Serial.parseInt();
      Serial.print("[RAM ");
      Serial.print(RamPos);
      Serial.print("] ");
      Serial.println(c);
      EEPROM.write(RamPos, c);
      RamPos += 1;
    }
  } else {
    RamPos = 0;
  }
 }
