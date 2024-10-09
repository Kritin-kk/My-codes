#include <U8g2lib.h>
#include <Wire.h>
#include <Arduino.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64  
  
U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0,U8X8_PIN_NONE); 

int bx = 0;
int bradius = 4 ;
int score = 0;
int lives = 3;
int ballval= random(2);
int bspeed = 2;
int gunLength = 15;
int BUTTON_PIN = 5;
float bs = 3.0;

void setup() {
  // put your setup code here, to run once:
  u8g2.begin();
  pinMode(BUTTON_PIN, INPUT);
  randomSeed(analogRead(A0));
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_6x10_tf);
  u8g2.drawStr(3,35,"Welcome To:");
  u8g2.drawStr(3,45,"Snowballer");
  u8g2.sendBuffer();
  delay(3000);
}

void loop() {
  u8g2.clearBuffer();
  u8g2.firstPage();

  u8g2.setFont(u8g2_font_unifont_t_symbols);
  u8g2.drawGlyph(1, 38, 0x2603);  /* dec 9731/hex 2603 Snowman */

  u8g2.setFont(u8g2_font_6x10_tf);
  u8g2.drawStr(1,8,"Lives:");
  u8g2.setCursor(38,8);
  u8g2.print(lives);
  u8g2.drawStr(1,59,"Score:");
  u8g2.setCursor(38,59);
  u8g2.print(score);




  Serial.println(digitalRead(BUTTON_PIN));  //debugging
  if(lives ==0){
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_6x10_tf);
    u8g2.drawStr(3,35,"Game Over!");
    u8g2.drawStr(3,45,"Score:");
    u8g2.setCursor(40,45);
    u8g2.print(score);
      
    u8g2.sendBuffer();

    return;
  }

  if(bx <= 125 && bx >= 99){
    bx = bx + bs;
    if (ballval == 1){
      u8g2.drawDisc(bx,32, bradius);
    }else if(ballval==0){
      u8g2.drawCircle(bx,32,bradius);
    }
  }else if (bx < 99){
    bx = bx  + bs;
    u8g2.drawBox(bx,28,8,8);
  }
  
  int value1 = digitalRead(BUTTON_PIN);

  if(digitalRead(BUTTON_PIN) == 1){
    u8g2.drawBox(123, 1, 5, 21);
    u8g2.drawBox(123, 42, 5, 21);
  }else if(value1 == 0){
    u8g2.drawBox(123, 1, 5, 21);
    u8g2.drawBox(123, 21, 5, 21);
    u8g2.drawBox(123, 42, 5, 21);
  }
  u8g2.sendBuffer();
  if(bx >= 125){
    if(digitalRead(BUTTON_PIN) == ballval){
      score = score + 1;
      u8g2.clearBuffer();
      u8g2.setFont(u8g2_font_6x10_tf);
      u8g2.drawStr(3,35,"Point!");
      u8g2.drawStr(3,45,"Score:");
      u8g2.setCursor(40,45);
      u8g2.print(score);
      u8g2.sendBuffer();
      ballval= random(2);
      bx = 0;
      bs = bs + 0.2;
      delay(1500);
    }else{
      lives = lives - 1;
      u8g2.clearBuffer();
      u8g2.setFont(u8g2_font_6x10_tf);
      u8g2.drawStr(3,35,"Live lost");
      u8g2.drawStr(3,45,"Lives:");
      u8g2.setCursor(40,45);
      u8g2.print(lives);
      u8g2.sendBuffer();
      ballval = random(2);
      bx = 0;
      delay(1500);
    }
  }
  delay(50);
    
}
