from pynput.keyboard import Key, Controller
import typer
import time
import os, sys

app = typer.Typer()

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
