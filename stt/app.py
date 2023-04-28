# this program will record audio while the button is pressed
# and then will transcribe it by hitting our api

import RPi.GPIO as GPIO

import audio.audio as audio
import simple_recorder.apa102 as apa102

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
            savedFileName = audioInstance.stopRecord(save=True, play=False)
            if savedFileName is not None:
                print("saved file: " + savedFileName)
    else:
        if not audioInstance.isRecording():
            turnOnLED()
            audioInstance.startRecord()
