# this program will record audio while the button is pressed
# and then will transcribe it by hitting our api

# NOTE: run export PYTHONPATH=$PYTHONPATH:$(pwd) to run this file from the root directory of the project
#  so that all different modules can be used

import RPi.GPIO as GPIO
import audio.audio as audio
import simple_recorder.apa102 as apa102
import requests

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
                print(response.text)
    else:
        if not audioInstance.isRecording():
            turnOnLED()
            audioInstance.startRecord()
