def modify_melody(file_path, new_melody):
    with open(
        __file__.replace("create_sketch.py", "playMelody_template.ino"), "r"
    ) as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("const PROGMEM int melody["):
                num_notes = len(new_melody)
                note_limit = 4677
                if num_notes > note_limit:
                    print(f"[WARN] Number of notes is {num_notes}, {num_notes-note_limit} greater than {note_limit} limit.")
                    print(f"[INFO] Writing only first {note_limit} notes.")
                    num_notes = note_limit
                file.write(f"const PROGMEM int melody[{num_notes}][3] = {{\n")
                for index, note_info in enumerate(new_melody):
                    if index >= num_notes:
                        break
                    note, duration, velocity = note_info
                    file.write(f"  {{ {note}, {duration}, {velocity} }},\n")
            else:
                file.write(line)
