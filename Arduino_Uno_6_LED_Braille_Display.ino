#include <Arduino.h>

//Output Pins
const int first_bit = 3;
const int second_bit = 4;
const int third_bit = 5;
const int fourth_bit = 6;
const int fifth_bit = 7;
const int sixth_bit = 8;

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
  pinMode(first_bit, OUTPUT);
  pinMode(second_bit, OUTPUT);
  pinMode(third_bit, OUTPUT);
  pinMode(fourth_bit, OUTPUT);
  pinMode(fifth_bit, OUTPUT);
  pinMode(sixth_bit, OUTPUT);


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
      digitalWrite(first_bit, LOW);
    }
    else if (braille[0] == '1'){
      digitalWrite(first_bit, HIGH);
    }

    if (braille[1] == '0'){
      digitalWrite(second_bit, LOW);
    }
    else if (braille[1] == '1'){
      digitalWrite(second_bit, HIGH);
    }

    if (braille[2] == '0'){
      digitalWrite(third_bit, LOW);
    }
    else if (braille[2] == '1'){
      digitalWrite(third_bit, HIGH);
    }

    if (braille[3] == '0'){
      digitalWrite(fourth_bit, LOW);
    }
    else if (braille[3] == '1'){
      digitalWrite(fourth_bit, HIGH);
    }

    if (braille[4] == '0'){
      digitalWrite(fifth_bit, LOW);
    }
    else if (braille[4] == '1'){
      digitalWrite(fifth_bit, HIGH);
    }

    if (braille[5] == '0'){
      digitalWrite(sixth_bit, LOW);
    }
    else if (braille[5] == '1'){
      digitalWrite(sixth_bit, HIGH);
    }

    delay(500);

    digitalWrite(first_bit, LOW);
    digitalWrite(second_bit, LOW);
    digitalWrite(third_bit, LOW);
    digitalWrite(fourth_bit, LOW);
    digitalWrite(fifth_bit, LOW);
    digitalWrite(sixth_bit, LOW);
  }

}
