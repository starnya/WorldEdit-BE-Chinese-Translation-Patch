import os
import polib

def get_lang(file):
    return os.path.splitext(file)[0]

def convert_file(in_path):
    lang = get_lang(in_path)
    newlines = []
    for entry in polib.pofile(in_path):
        if entry.msgid != "":
            string = entry.msgstr.replace('\\"', '"')
            if "\n" in string:
                sys.exit(
                    f'Error: New line detected in translation string "{entry.msgid}" in file "{in_path}"!'
                )
            newlines.append(f"{entry.msgid}={string}\t#\n")
    newlines[-1] = newlines[-1][:-1]

    with open(f"{lang}.lang", "w", encoding="utf-8") as file:
        file.writelines(newlines)
        print(f"{in_path} converted to {lang}.lang")

for file in os.listdir('.'):
    if file.endswith('.po'):
        convert_file(file)