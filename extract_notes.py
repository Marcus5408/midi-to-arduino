import mido
import math

def midi_to_arduino_data(midi_file, output_file, header_file):
    mid = mido.MidiFile(midi_file)

    # MIDI note numbers to frequency mapping (A4 = 440 Hz)
    note_to_freq = {i: 440 * 2 ** ((i - 69) / 12) for i in range(128)}

    # Dictionary to store unique notes
    unique_notes = {}

    # Compute the tempo
    ticks_per_beat = mid.ticks_per_beat
    tempo = 500000
    for t in mid.tracks:
        for m in t:
            if m.type == "set_tempo":
                tempo = m.tempo
                break

    with open(header_file, "w") as hf:
        hf.write("#ifndef NOTES_H\n\n")

        with open(output_file, "w") as f:
            # Go through all messages in the track
            time = 0
            for msg in mid.tracks[0]:
                time += msg.time
                if msg.type == "note_on":
                    note = msg.note
                    freq = int(note_to_freq[note])
                    ms_per_tick = (tempo / 1000) / ticks_per_beat
                    duration = int(msg.time * ms_per_tick)
                    velocity = int(msg.velocity)
                    if duration != 0:
                        if note not in unique_notes:
                            unique_notes[note] = freq
                            hf.write(f"#define NOTE_{note} {freq}\n")
                        f.write(f"{{ NOTE_{note}, {duration}, {velocity} }},\n")

        hf.write("\n#endif // NOTES_H\n")
