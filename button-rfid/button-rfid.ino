#include <SPI.h>
#include <MFRC522.h>

// Define button pins
const int button1Pin = 4;  // Button 1 pin
const int button2Pin = 5;  // Button 2 pin
const int button3Pin = 6;  // Button 3 pin
const int button4Pin = 7;  // Button 4 pin

// Variables to track button states
int button1State = LOW;  // Initial state (HIGH because of INPUT_PULLUP)
int button2State = LOW;  // Initial state (HIGH because of INPUT_PULLUP)
int button3State = LOW;  // Initial state (HIGH because of INPUT_PULLUP)
int button4State = LOW;  // Initial state (HIGH because of INPUT_PULLUP)

// RFID settings
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.

void setup() {
  Serial.begin(9600);       // Initialize serial communication
  SPI.begin();              // Initiate SPI bus
  mfrc522.PCD_Init();      // Initiate MFRC522

  // Initialize button pins
  pinMode(button1Pin, INPUT_PULLUP);  // Set button 1 pin as input with internal pull-up resistor
  pinMode(button2Pin, INPUT_PULLUP);  // Set button 2 pin as input with internal pull-up resistor
  pinMode(button3Pin, INPUT_PULLUP);  // Set button 3 pin as input with internal pull-up resistor
  pinMode(button4Pin, INPUT_PULLUP);  // Set button 4 pin as input with internal pull-up resistor
 
  Serial.println("Scan a card and then press a button");
}

void loop() {
  // Check if a new card is present
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    // Print the UID
    String uidString = "";
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      uidString += String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : "");
      uidString += String(mfrc522.uid.uidByte[i], HEX);
    }
    uidString.toUpperCase();

    // Inform the user to press a button
    Serial.print("Card UID detected: ");
    Serial.println(uidString);
    Serial.println("Press a button to continue...");

    bool buttonPressed = false;  // Flag to check if a button was pressed

    while (!buttonPressed) {
      // Read the state of the buttons
      int currentButton1State = digitalRead(button1Pin);
      int currentButton2State = digitalRead(button2Pin);
      int currentButton3State = digitalRead(button3Pin);
      int currentButton4State = digitalRead(button4Pin);

      // Check if Button 1 is pressed
      if (currentButton1State == LOW && button1State == HIGH) {
        Serial.print(uidString);
        Serial.println(";Not Sure");  // Output UID and Button 1
        buttonPressed = true;
      }

      // Check if Button 2 is pressed
      else if (currentButton2State == LOW && button2State == HIGH) {
        Serial.print(uidString);
        Serial.println(";Sad");  // Output UID and Button 2
        buttonPressed = true;
      }

      // Check if Button 3 is pressed
      else if (currentButton3State == LOW && button3State == HIGH) {
        Serial.print(uidString);
        Serial.println(";Fine");  // Output UID and Button 3
        buttonPressed = true;
      }

      // Check if Button 4 is pressed
      else if (currentButton4State == LOW && button4State == HIGH) {
        Serial.print(uidString);
        Serial.println(";Joyful");  // Output UID and Button 4
        buttonPressed = true;
      }

      // Update button states
      button1State = currentButton1State;
      button2State = currentButton2State;
      button3State = currentButton3State;
      button4State = currentButton4State;

      delay(50);  // Increase delay for better debounce
    }

    // Stop reading the card
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();

    // Add a small delay to prevent detecting the same card again immediately
    delay(500); // Adjust delay as needed
  }
}
