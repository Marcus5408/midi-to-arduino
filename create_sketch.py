real_code = """
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

void loop() {
  int melodyLength = sizeof melody / sizeof melody[0];
  for (int i = 0; i < melodyLength; i++) {
    int frequency = pgm_read_word(&melody[i][0]);
    long duration = pgm_read_word(&melody[i][1]);
    int velocity = pgm_read_word(&melody[i][2]);

    Serial.print("Frequency: ");
    Serial.print(frequency);
    Serial.print(" Duration: ");
    Serial.print(duration);
    Serial.print(" Velocity: ");
    Serial.println(velocity);

    buzz(frequency, duration, velocity);
  }
  delay(3000);
}
"""

def modify_melody(file_path, new_melody):
    with open(__file__.replace("create_sketch.py", "playMelody_template.ino"), "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("const PROGMEM int melody["):
                num_notes = len(new_melody)
                file.write(f"const PROGMEM int melody[{num_notes}][3] = {{\n")
                for note, duration, velocity in new_melody:
                    file.write(
                        f"  {{ {note}, {duration}, {velocity} }},\n"
                    )
            else:
                file.write(line)