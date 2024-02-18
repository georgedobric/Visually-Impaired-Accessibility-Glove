
#include <Arduino.h>
#include <Servo.h>
Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;
Servo Servo5;
Servo Servo6;
//Output Pins



const char* brailleAlphabet[26] = {
  "100000", "110000", "100100", "100110", "100010",
  "110100", "110110", "110010", "010100", "010110",
  "101000", "111000", "101100", "101110", "101010",
  "111100", "111110", "111010", "011100", "011110",
  "101001", "111001", "010111", "101101", "101111",
  "101011"
};

int asciiUpperCase[26];

void initializeAsciiUpperCase() {
  // Initialize the ASCII values for uppercase letters 'A' to 'Z'
  for (int i = 0; i < 26; i++) {
    asciiUpperCase[i] = 'A' + i;
  }
}

const char* getBrailleFromAscii(char asciiChar) {
  // Lookup the Braille representation for the ASCII character
  if (asciiChar >= 'A' && asciiChar <= 'Z') {
    return brailleAlphabet[asciiChar - 'A'];
  } else {
    // Return an empty string if ASCII value is not found
    return "";
  }
}

void setup() {



  Serial.begin(9600);

  //Set output pins
  Servo1.attach(2);
  Servo2.attach(3);
  Servo3.attach(4);
  Servo4.attach(5);
  Servo5.attach(6);
  Servo6.attach(7);


  


  initializeAsciiUpperCase();

  // Test the hash table
  for (int i = 0; i < 26; i++) {
    char asciiChar = 'A' + i;
    const char* braille = getBrailleFromAscii(asciiChar);
    // Serial.print(asciiChar);
    // Serial.print(": ");
    // Serial.println(braille);
  }
}

void loop() {
  delay(3000);
  String text = "ABCDEF";
  for (int i = 0; i < text.length(); i++) {
    char asciiChar = text.charAt(i);
    const char* braille = getBrailleFromAscii(asciiChar);
    delay(1000);
    Serial.print(text[i]);
    Serial.print(": ");
    Serial.println(braille);
    Serial.println(braille[0]);
    Serial.println(braille[1]);
    Serial.println(braille[2]);
    Serial.println(braille[3]);
    Serial.println(braille[4]);
    Serial.println(braille[5]);

    // String bit1, bit2, bit3, bit4, bit5, bit6;

    if (braille[0] == '0'){
       
    }
    else if (braille[0] == '1'){
       for (int i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo1.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0; i -= 1) { // goes from 180 degrees to 0 degrees
    Servo1.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    if (braille[1] == '0'){
      
    }
    else if (braille[1] == '1'){
     for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo2.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0; i -= 1) { // goes from 180 degrees to 0 degrees
    Servo2.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    if (braille[2] == '0'){
      
    }
    else if (braille[2] == '1'){
       for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo3.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0; i -= 1) { // goes from 180 degrees to 0 degrees
    Servo3.write(i);             // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    if (braille[3] == '0'){
     
    }
    else if (braille[3] == '1'){
      for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo4.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0;  i -= 1) { // goes from 180 degrees to 0 degrees
    Servo4.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    if (braille[4] == '0'){
     
    }
    else if (braille[4] == '1'){
      for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo5.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0; i -= 1) { // goes from 180 degrees to 0 degrees
    Servo5.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    if (braille[5] == '0'){
    
     }
    else if (braille[5] == '1'){
     for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Servo6.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (i = 180; i >= 0; i -= 1) { // goes from 180 degrees to 0 degrees
    Servo6.write(i);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
    }

    delay(500);

    
  }

}