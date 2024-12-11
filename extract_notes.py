import mido
import math


def midi_to_arduino_data(midi_file, output_file):
    mid = mido.MidiFile(midi_file)

    # MIDI note numbers to frequency mapping (A4 = 440 Hz)
    note_to_freq = {i: 440 * 2 ** ((i - 69) / 12) for i in range(128)}

    # Check tracks of the MIDI file using mido.checks
    
    
    # Compute the tempo
    ticks_per_beat = mid.ticks_per_beat
    tempo = 500000
    for t in mid.tracks:
        for m in t:
            if m.type == "set_tempo":
                tempo = m.tempo
                break

    with open(output_file, "w") as f:
        # Go through all messages in the track
        time = 0
        for msg in mid.tracks[0]:
            time += msg.time
            if msg.type == "note_on":
                freq = int(note_to_freq[msg.note])
                ms_per_tick = (tempo / 1000) / ticks_per_beat
                duration = int(msg.time * ms_per_tick)
                velocity = int(msg.velocity)
                if duration != 0:
                    f.write(f"{'{ '}{freq}, {duration}, {velocity}{' }'},\n")
    
    # # old implementation
    # with open(output_file, "w") as f:
    #     for track in mid.tracks:
    #         time = 0
    #         for msg in track:
    #             time += msg.time
    #             if msg.type == "note_on":
    #                 freq = int(note_to_freq[msg.note])
    #                 ticks_per_beat = mid.ticks_per_beat
    #                 tempo = 500000  # Default tempo in microseconds per beat (120 BPM)
    #                 for t in mid.tracks:
    #                     for m in t:
    #                         if m.type == "set_tempo":
    #                             tempo = m.tempo
    #                             break
    #                 ms_per_tick = (tempo / 1000) / ticks_per_beat
    #                 duration = int(msg.time * ms_per_tick)  # Convert to milliseconds
    #                 velocity = int(msg.velocity)
    #                 if duration != 0:
    #                     f.write(f"{'{ '}{freq}, {duration}, {velocity}{' }'},\n")
