""" product
- (todo) keep recording in 5 second intervals
simple algorithm. start recording, send to server after 5 seconds
combine with currentTextBlock, and keep appending

process currentTextBlock every 5 seconds, and if fits command, then execute and clear currentTextBlock
clear currentTextBlock after 200 characters as well

* show a light when sending to server for transcription

- hey rameelo, how long will I live?
- good morning!
"""

import time

import RPi.GPIO as GPIO

import audio.audio as audio
import tts.app as tts
import requests
from datetime import datetime
import simple_recorder.apa102 as apa102

API_URL = "http://192.168.50.159:5001/transcribe"

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

audioInstance = audio.Audio()
# number of pixels on the LED strip on the hat
PIXELS_N = 3
led = apa102.APA102(num_led=PIXELS_N)


def turnOffLED():
    led.clear_strip()
    led.show()


def turnOnLED():
    for i in range(PIXELS_N):
        led.set_pixel(i, 255, 192, 203)
    led.show()


# see if we should execute a certain command based on the current text block
def process(text):
    formatted = text.lower()
    if "live" in text and "how long" in formatted:
        # get the number of days left until 2058
        daysLeftHeran = (datetime(2057, 1, 1) - datetime.now()).days
        daysLeftKam = (datetime(2043, 1, 1) - datetime.now()).days
        daysLeftArjun = (datetime(2070, 1, 1) - datetime.now()).days

        tts.say(
            f"Heran, you have {daysLeftHeran} days left to live. Kam, you have {daysLeftKam} days left to live. Arjun, you have {daysLeftArjun} days left to live.")
    elif "good morning" in formatted:
        dt = datetime.now()
        dayOfWeek = dt.strftime('%A')
        full_month_name = dt.strftime("%B")
        tts.say(
            f"Good morning! Today is {dayOfWeek}, {full_month_name}, {dt.day}, {dt.year}.")
    else:
        tts.say("Sorry, I don't understand that command")


tts.say("hello, how can I help you today?")

if __name__ == '__main__':
    while True:
        state = GPIO.input(BUTTON)

        if state:
            if audioInstance.isRecording():
                turnOffLED()
                savedFileName = audioInstance.stopRecord(save=True, play=True)
                if savedFileName is not None:
                    print("saved file: " + savedFileName)
                    # make a request with the saved file to the api
                    response = requests.request(
                        "POST", API_URL, files={"file": open(savedFileName, "rb")}
                    )
                    print(response.json())
                    results = response.json()["results"]
                    command = results[0]["transcript"]
                    process(command)
        else:
            if not audioInstance.isRecording():
                turnOnLED()
                audioInstance.startRecord()
