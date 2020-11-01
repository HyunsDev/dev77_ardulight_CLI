#include <EEPROM.h>
#include <Adafruit_NeoPixel.h>
#define PIN 7

#define NUM_LEDS 20

int led_l =  12;
int RamPos = 0;
int ledMode = EEPROM.read(0);
int ii_0 = 0;
int ii_8 = 2;
bool needUpdate = false;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  pinMode(led_l, OUTPUT);
  Serial.begin(9600);
  strip.begin(); //네오픽셀을 초기화하기 위해 모든LED를 off시킨다
  strip.show();
}

void loop() {
  int ledMode = EEPROM.read(0);

  Serial.print(ledMode);
  Serial.print(" ");
  Serial.print(EEPROM.read(1));
  Serial.print(" ");
  Serial.print(EEPROM.read(2));
  Serial.print(" ");
  Serial.print(EEPROM.read(3));
  Serial.print(" ");
  Serial.println(EEPROM.read(4));

  if (ledMode == 8) {
    digitalWrite(led_l, LOW);
  } else {
    digitalWrite(led_l, HIGH);
  }

  if (ledMode == 9) { //Mode on
    for (int i = 0; i < NUM_LEDS; i++) {
      if (ii_0 == 0) {
        strip.setPixelColor(i, 255, 0, 0);
      } else if (ii_0 == 1) {
        strip.setPixelColor(i, 0, 255, 0);
      } else {
        strip.setPixelColor(i, 0, 0, 255);
      }

      strip.show();
      delay(50);
    }

    if (ii_0 == 0) {
      ii_0 = 1;
    } else if (ii_0 == 1) {
      ii_0 = 2;
    } else {
      ii_0 = 0;
    }
  }

  else if (ledMode == 1) { //Mode off =======
    if (needUpdate) {
      needUpdate = true;
      for (int i = 0; i < NUM_LEDS; i++) {
        strip.setPixelColor(i, 0, 0, 0);
      }
      strip.show();
    }
  }

  else if (ledMode == 2) { //솔리드 ========
    if (needUpdate) {
      needUpdate = true;
      for (int i = 0; i < NUM_LEDS; i++) {
        strip.setPixelColor(i, EEPROM.read(2), EEPROM.read(3), EEPROM.read(4));
      }
      strip.show();

    }

  }

  else if (ledMode == 3) { //개별 적용 =======
    if (needUpdate) {
      needUpdate = true;
      int ii = 2;
      for (int i = 0; i < NUM_LEDS; i++) {
        strip.setPixelColor(i, EEPROM.read(ii), EEPROM.read(ii + 1), EEPROM.read(ii + 2));
        ii = ii + 3;
      }
      strip.show();
    }
  }

  else if (ledMode == 4) { //스팩트럼 =======
    rainbow(EEPROM.read(1));
  }

  else if (ledMode == 5) { //숨쉬기 =======
    // if(needUpdate) {
    //   needUpdate = true;
    //   for (int i = 0; i < NUM_LEDS; i++) { //픽셀 컬러
    //     strip.setPixelColor(i, EEPROM.read(2), EEPROM.read(3), EEPROM.read(4));
    //   }
    // }


    // int x = 1;

    // for (int i_0 = 0; i_0 > -1; i_0 = i_0 + x) { //밝기
    //   Serial.print("5_");
    //   Serial.println(i_0);
    //   strip.setBrightness(i_0);
    //   if (i_0 == 255) {
    //     x = -1;
    //   }
    //   strip.show();
    //   delay(EEPROM.read(1));
    // }

    for (int i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, 255, 0, 0);
      strip.show();
    }
  }

  else if (ledMode == 6) { //웨이브
    rainbowCycle(EEPROM.read(1));
  }

  else if (ledMode == 7) { //Down
    theaterChase(strip.Color(EEPROM.read(2), EEPROM.read(3), EEPROM.read(4)), EEPROM.read(1));
  }

  else if (ledMode == 8) { //컬러 와이프
    for (int i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, EEPROM.read(ii_8), EEPROM.read(ii_8 + 1), EEPROM.read(ii_8 + 2));
      strip.show();
      delay(EEPROM.read(1));
    }

    if (ii_8 < 43) {
      ii_8 = ii_8 + 3;
    } else {
      ii_8 = 2;
    }
  }
}

void serialEvent() { //메모리 입력 구문
  commandread();
}

void commandread() { //시리얼 버퍼
  //시리얼 버퍼 이슈 있음, 로컬 판에서 해결 (버퍼 크기를 늘림)
  //https://www.notion.so/hnhs/CLI-be3cd6c45daa431bad3b7f4bcead0b16#b1c2e6bd62934703aed99ca10bd5f321
  //참고

  RamPos = 0;

  if (Serial.available()) {
    needUpdate = true;
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
  }
}

void rainbow(uint8_t wait) { //레인보우 스펙트럼
  uint16_t i, j;
  for (j = 0; j < 256; j++) {
    for (i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, Wheel((i + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

uint32_t Wheel(byte WheelPos) { //컬러 휠
  if (WheelPos < 85) {
    return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if (WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
    WheelPos -= 170;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

// void theaterChaseRainbow(uint8_t wait) { //LED를 다양한색으로 표현하며 깜빡거린다
//   for (int j=0; j < 256; j++) {     //256가지의 색을 표현
//     for (int q=0; q < 3; q++) {
//         for (int i=0; i < strip.numPixels(); i=i+3) {
//           strip.setPixelColor(i+q, Wheel( (i+j) % 255));
//         }
//         strip.show();

//         delay(wait);

//         for (int i=0; i < strip.numPixels(); i=i+3) {
//           strip.setPixelColor(i+q, 0);
//         }
//     }
//   }
// }

void theaterChase(uint32_t c, uint8_t wait) { //입력한 색으로 LED를 깜빡거리며 표현한다
  for (int j = 0; j < 10; j++) { //do 10 cycles of chasing
    for (int q = 0; q < 3; q++) {
      for (int i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, c);  //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (int i = 0; i < strip.numPixels(); i = i + 3) {
        strip.setPixelColor(i + q, 0);      //turn every third pixel off
      }
    }
  }
}

void rainbowCycle(uint8_t wait) { //NeoPixel에 달린 LED를 각각 다른색으로 시작하여 다양한색으로 반복한다
  uint16_t i, j;

  for (j = 0; j < 256; j++) {
    for (i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// void colorWipe(uint32_t c, uint8_t wait) { //NeoPixel에 달린 LED를 각각 주어진 인자값 색으로 채워나가는 함수
//   for(uint16_t i=0; i<strip.numPixels(); i++) {
//       strip.setPixelColor(i, c);
//       strip.show();
//       delay(wait);
//   }
// }
