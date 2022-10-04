from pynput.keyboard import Key, Controller
import typer
import time
import pathlib
import os

app = typer.Typer()

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


# Read file and return text
def read_file(file):
    with open(file, 'r') as f:
        return f.read()


# Splits text into lines
def split(text):
    return [line for line in text]


# Auto type text
@app.command()
def autotype(file: str, s: float = 0.05):

    text = read_file(file)

    # Controls keyboard
    keyboard = Controller()

    # Wait for cursor placement
    time.sleep(5)

    # Type file
    for line in text:
        keyboard.type(line)
        time.sleep(s)


if __name__ == "__main__":
    app()
