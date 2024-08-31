#include <Adafruit_GFX.h>
#include <MCUFRIEND_kbv.h>

MCUFRIEND_kbv tft;

void setup() {
  tft.begin();
  tft.setRotation(1); // Adjust the rotation if needed

  // Set the background color to black
  tft.fillScreen(0x0000);

  // Set the colors
  uint16_t outerCircleColor = 0xFFFF; // White
  uint16_t blackColor = 0x0000;       // Black
  uint16_t smallCircleColor = 0xFFFF; // White for the small circle

  // Draw the initial crescent shape
 // drawCrescent(160, 120, 70, 40, outerCircleColor, blackColor, smallCircleColor);
 // delay(100);
  // Draw the new crescent effect
 // newCrescent(177, 150, 90, outerCircleColor);
 // delay(300);
 // drawCrescent(160, 120, 70, 40, outerCircleColor, blackColor, smallCircleColor);
}

void loop() {
  uint16_t outerCircleColor = 0xFFFF; // White
  uint16_t blackColor = 0x0000;       // Black
  uint16_t smallCircleColor = 0xFFFF; // Wh
  eyes(160, 120, 70, 40, outerCircleColor, blackColor, smallCircleColor);
  delay(610);
  //Draw the new crescent effect
  blinking(177, 155, 90, outerCircleColor);
  delay(450);
  eyes(160, 120, 70, 40, outerCircleColor, blackColor, smallCircleColor);
  delay(200);
  //movement left
  move_left();
  delay(800);
 
}

void eyes(int x, int y, int outerRadius, int innerRadius, uint16_t outerColor, uint16_t innerColor, uint16_t smallCircleColor) {
  // Draw the outer circle
  tft.fillCircle(x, y, outerRadius, outerColor);

  // Draw the inner circle with background color to create the crescent effect
  tft.fillCircle((x + innerRadius / 2)-20, y, innerRadius, innerColor);

  // Draw the small white circle
  int smallCircleRadius = 10; // Radius of the small white circle
  int smallCircleX = x + innerRadius / 2 + smallCircleRadius * 2; // X position for the small white circle
  int smallCircleY = y - innerRadius / 2 + smallCircleRadius + 20; // Y position for the small white circle
  tft.fillCircle(smallCircleX-20, smallCircleY, smallCircleRadius, smallCircleColor);
}

// Animation of the eyes (blinking)
void blinking(int x, int y, int outerRadius, uint16_t outerColor) {
  uint16_t blackColor = 0x0000; // Black color for the crescent effect
  int blackCircleRadius = outerRadius * 0.9; // Radius of the circle covering 90% of the outer circle
  
  // Draw the outer circle
  tft.fillCircle(160, 120, 70, outerColor);

  // Draw the black circle to create the crescent effect
  tft.fillCircle(x - outerRadius / 5, y, blackCircleRadius, blackColor);
}

//move left eyes animation 
void move_left() {
  uint16_t outerCircleColor = 0xFFFF; // White
  uint16_t blackColor = 0x0000;       // Black
  uint16_t smallCircleColor = 0xFFFF;

  // Clear the current eyes
  //eyes(140, 120, 70, 40, outerCircleColor, blackColor, smallCircleColor);
   tft.fillCircle(160, 120, 70, 0xFFFF);
  tft.fillCircle(135 , 120, 40, 0x0000);
  tft.fillCircle(155, 130, 10,0xFFFF );


  // Update the eye position
  }

//void happy(int x, int y, int outerRadius, uint16_t outerColor) {
 // uint16_t blackColor = 0x0000; // Black color for the crescent effect
  //int blackCircleRadius = outerRadius * 0.9; // Radius of the circle covering 90% of the outer circle
  
   //Draw the outer circle
 // tft.fillCircle(160, 120, 70, outerColor);

   //Draw the black circle to create the crescent effect
  //tft.fillCircle(x - outerRadius / 5, y, blackCircleRadius, blackColor);
//}