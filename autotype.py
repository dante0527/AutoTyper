from pynput.keyboard import Key, Controller
import os, sys, time
import typer
import pathlib


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
    with open(f"{os.getcwd()}/{file}", 'r') as f:
        return f.read()


# Auto type text
@app.command()
def autotype(file: str, speed: float = 0.04):

    text = read_file(file)

    # Controls keyboard
    keyboard = Controller()

    # Wait for cursor placement
    time.sleep(5)

    # Type file
    for line in text:
        keyboard.type(line)
        time.sleep(speed)


if __name__ == "__main__":
    app()
