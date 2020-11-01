#include <EEPROM.h>
int RamPos = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(EEPROM.read(0));
  Serial.print(" ");
  Serial.print(EEPROM.read(1));
  Serial.print(" ");
  Serial.print(EEPROM.read(2));
  Serial.print(" ");
  Serial.print(EEPROM.read(3));
  Serial.print(" ");
  Serial.println(EEPROM.read(4));
}

void serialEvent() {

  RamPos = 0;

  if (Serial.available()) {
    while (Serial.available()) {
      int c = Serial.parseInt();

      if ( c == 0 && RamPos == 0) {
        ;
      } else {
        Serial.print("[RAM ");
        Serial.print(RamPos);
        Serial.print("] ");
        Serial.println(c);
        EEPROM.write(RamPos, c);
      }

      RamPos += 1;
    }
  } else {
    RamPos = 0;
  }
 }
