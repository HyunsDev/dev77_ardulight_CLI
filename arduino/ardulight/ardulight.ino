
#include <EEPROM.h>
#define PIN 7
#define NUM_LEDS 14

int RamPos = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);
}

void loop() {
  if(Serial.available()) { //메모리 입력 구문
    int c = Serial.parseInt();
    Serial.print("[RAM ");
    Serial.print(RamPos);
    Serial.print("] ");
    Serial.println(c);
    EEPROM.write(RamPos, c);
   RamPos += 1;
  } else {
    RamPos = 0;
  }
  
  int ledMode = EEPROM.read(0);
  
  
  
}