#include <Arduino.h>
#include <Servo.h>

Servo servos[6];

const char* brailleAlphabet[26] = {
"100000", "110000", "100100", "100110", "100010",
"110100", "110110", "110010", "010100", "010110",
"101000", "111000", "101100", "101110", "101010",
"111100", "111110", "111010", "011100", "011110",
"101001", "111001", "010111", "101101", "101111",
"101011"
};

const char* getBrailleFromAscii(char asciiChar) {
  if (asciiChar >= 'A' && asciiChar <= 'Z') {
    return brailleAlphabet[asciiChar - 'A'];
  }
  else {
    Serial.print("Can't find");
    return "";
  }
}

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 6; ++i)
  {
    servos[i].attach(i + 2);
    servos[i].write(0);
  }
}

void loop() {
  String text = "AB";
  for (int i = 0; i < text.length(); ++i) {
    char asciiChar = text.charAt(i);
    const char* braille = getBrailleFromAscii(asciiChar);
    Serial.print(text[i]);
    Serial.print(i);
    Serial.print(": ");
    Serial.println(braille);
    delay(1000);

    for (int j = 0; j <= 180; ++j)
    {
      for (int k = 0; k < 6; k++)
      {
        if (braille[k] == '1')
          servos[k].write(j);
      }

      delay(15);
    }

    for (int j = 180; j >= 0; --j)
    {
      for (int k = 0; k < 6; k++)
      {
        if (braille[k] == '1')
          servos[k].write(j);
      }

      delay(15);
    }

    delay(500);
  }
}
