# this program will record audio while the button is pressed
# it will then play the audio back to the user from memory

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

while True:
    state = GPIO.input(BUTTON)

    if state:
        if audioInstance.isRecording():
            audioInstance.stopRecord()
    else:
        if not audioInstance.isRecording():
            audioInstance.startRecord()
