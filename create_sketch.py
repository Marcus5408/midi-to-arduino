import os


def modify_melody(file_path, new_melody):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.strip().startswith("const PROGMEM int melody["):
                num_notes = len(new_melody)
                file.write(f"const PROGMEM int melody[{num_notes}][3] = {{\n")
                for note in new_melody:
                    file.write(
                        f"  {{ {note}, 0, 0 }},\n"
                    )
                file.write("};\n")
            else:
                file.write(line)
