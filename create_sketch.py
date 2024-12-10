def modify_melody(file_path, new_melody):
    with open(
        __file__.replace("create_sketch.py", "playMelody_template.ino"), "r"
    ) as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("const PROGMEM int melody["):
                num_notes = len(new_melody)
                file.write(f"const PROGMEM int melody[{num_notes}][3] = {{\n")
                for note, duration, velocity in new_melody:
                    file.write(f"  {{ {note}, {duration}, {velocity} }},\n")
            else:
                file.write(line)
