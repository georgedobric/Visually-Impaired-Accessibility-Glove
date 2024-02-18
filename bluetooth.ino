#include <SoftwareSerial.h>

SoftwareSerial bluetooth(5, 6);

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
  // Check if it's time to send a message (every 5 seconds)
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= 5000) {
    // Send the message to the Bluetooth module
    bluetooth.println("Hello, from Arduino!");
    // Update the previousMillis variable
    previousMillis = currentMillis;
  }
  
  // Check for incoming messages from the phone
  if (bluetooth.available()) {
    Serial.write(bluetooth.read());
  }
  
  // Check for messages to send to the phone
  if (Serial.available()) {
    bluetooth.write(Serial.read());
  }
}
