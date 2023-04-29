# this program will record audio while the button is pressed
# and then will transcribe it by hitting our api

# NOTE: run export PYTHONPATH=$PYTHONPATH:$(pwd) to run this file from the root directory of the project
#  so that all different modules can be used

import audio.audio as audio
import requests

API_URL = "http://192.168.50.159:5001/tts"

audioInstance = audio.Audio()

response = requests.post(API_URL, data={'text': 'hello world'})
print(response)

# get the file data from the response
# write the file data to a file
# save the file

# play the file
audioInstance.playFile('audio.wav')
