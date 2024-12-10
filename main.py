import os
from create_sketch import modify_melody
from extract_notes import midi_to_arduino_data


def main():
    # Paths to the files
    midi_file_path = os.path.join(os.path.dirname(__file__), "midi", "Matsuri.mid")
    ino_file_path = os.path.join(
        os.path.dirname(__file__), "playMelody", "playMelody.ino"
    )
    output_file_path = os.path.join(os.path.dirname(__file__), "notedata.txt")

    # Extract notes from MIDI file and save to output file
    midi_to_arduino_data(midi_file_path, output_file_path)

    # Read the extracted notes
    new_melody = []
    with open(output_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip("{} \n").split(",")
            note = int(parts[0].strip())
            duration = int(parts[1].strip())
            velocity = int(parts[2].strip("{} "))
            new_melody.append((note, duration, velocity))

    # Modify the melody in the .ino file
    modify_melody(ino_file_path, new_melody)


if __name__ == "__main__":
    main()
