from time import sleep
from sys import stdout


def timed_writing(text):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(0.06)
