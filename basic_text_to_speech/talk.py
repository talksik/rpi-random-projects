import time

import os

import RPi.GPIO as GPIO
import time

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)


def robot(text):
    print("executing command")
    os.system("espeak -w output.wav \"" + text + "\"")
    os.system("aplay -D plughw:2,0 output.wav")


def sayScript():
    print("initializing")
    robot("hey Heran?")
    robot("Based on your age, health, and habits, you have 10950 days left")
    robot("Make sure you chant more")
    time.sleep(5)

    robot("hey Kam?")
    robot("you have some time, but make sure to surrender to jesus")
    time.sleep(5)

    robot("hey Arjun")
    robot("You have maybe 12000 days left to live")
    robot("just drink some water or something")


if __name__ == '__main__':
    while True:
        try:
            state = GPIO.input(BUTTON)
            if state:
                print("off")
            else:
                print("on")
                sayScript()

        except KeyboardInterrupt:
            break

    time.sleep(1)
