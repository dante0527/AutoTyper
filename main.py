from pynput.keyboard import Key, Controller
import time
import pathlib
import os

# Convert .py to .txt and return text
def py_to_txt(file):

    # Convert Python script to .txt
    with open(file, 'r'):

        # Filename stem
        stem = f"{pathlib.Path(file).stem}"

        # Copy file.py to file.txt
        os.system(f"cp {file} {stem}.txt")

    # Read text from file.txt
    with open(f"{stem}.txt", 'r') as ftxt:
        text = ftxt.read()
    
    return text


# Splits text into lines
def split(text):
    return [line for line in text]


# Auto type text
def autotype(text):

    # Controls keyboard
    keyboard = Controller()

    # Wait for cursor placement
    time.sleep(3)

    # Type file
    for word in split(text):
        keyboard.type(word)
        time.sleep(0.05)


if __name__ == "__main__":
    autotype(py_to_txt("tia.py"))
