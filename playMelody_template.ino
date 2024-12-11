/*
2.07 - Challenge 2: Jingle all the Way
--------------------------------------
By Issac Liu, Pd 7/8 Odd
12/8/2024

Uses a void-type function to buzz,
playing out a melody.
*/

#include "notes.h"

// Set up the melody array.
// Each row contains a frequency, duration, and velocity.
// The melody array tends to be too large to fit in SRAM,
// so it is stored in PROGMEM instead.
const PROGMEM int melody[2464][3] = {
};
int passBuzzer = 9;

void setup() {
  pinMode(passBuzzer, OUTPUT);
  Serial.begin(9600);
}

void buzz(int frequency, int duration, int velocity) {
  // Map the velocity (0-127) to a duty cycle (0-255)
  int dutyCycle = map(velocity, 0, 127, 0, 255);

  // Play the tone with the calculated duty cycle
  analogWrite(passBuzzer, dutyCycle);
  tone(passBuzzer, frequency, duration);
  delay(duration);
  noTone(passBuzzer);
  analogWrite(passBuzzer, 0);
}

// Calculate the length of the melody array
int melodyLength = sizeof melody / sizeof melody[0];
void loop() {
  // Iterate through the melody array
  for (int i = 0; i < melodyLength; i++) {
    // Read the frequency, duration, and velocity from the melody array.
    // Because the melody array is stored in PROGMEM, we use pgm_read_word
    // to read the values.
    int frequency = pgm_read_word(&melody[i][0]);
    long duration = pgm_read_word(&melody[i][1]);
    int velocity = pgm_read_word(&melody[i][2]);

    // Debug print the frequency, duration, and velocity
    Serial.print("Frequency: ");
    Serial.print(frequency);
    Serial.print(" Duration: ");
    Serial.print(duration);
    Serial.print(" Velocity: ");
    Serial.println(velocity);

    // Play the note
    buzz(frequency, duration, velocity);
  }
  // Restart the melody after a 3 second delay
  delay(3000);
}
