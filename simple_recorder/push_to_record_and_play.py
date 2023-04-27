# this program will record audio while the button is pressed
# it will then play the audio back to the user from memory

import apa102
import RPi.GPIO as GPIO

# importing sys
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/home/talksik/rpi-random-projects/audio')

import audio


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
        led.set_pixel_rgb(i, 0, 0, 255)
    led.show()


while True:
    state = GPIO.input(BUTTON)

    if state:
        if audioInstance.isRecording():
            audioInstance.stopRecord()
            turnOffLED()
    else:
        if not audioInstance.isRecording():
            audioInstance.startRecord()
            turnOnLED()
