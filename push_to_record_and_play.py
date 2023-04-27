# this program will record audio while the button is pressed
# it will then play the audio back to the user from memory

import audio
import RPi.GPIO as GPIO

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

audioInstance = audio.Audio()

while True:
    state = GPIO.input(BUTTON)
    if audioInstance.isRecording():
        audioInstance.readChunk()

    if state:
        print("button: OFF")
        if audioInstance.isRecording():
            audioInstance.stopRecord()
    else:
        print("button: ON")
        if not audioInstance.isRecording():
            audioInstance.startRecord()
