# this program will record audio while the button is pressed
# and then will transcribe it by hitting our api

# NOTE: run export PYTHONPATH=$PYTHONPATH:$(pwd) to run this file from the root directory of the project
#  so that all different modules can be used

import audio.audio as audio
import requests

API_URL = "http://192.168.50.159:5001/tts"

audioInstance = audio.Audio()

# send request with json
headers = {
    "Content-type": "application/json",
}
response = requests.post(
    API_URL,
    headers=headers,
    json={"text": "hello world. the weather today is sunny."}
)

# get the file data from the response and write to temp local file
fileName = "output.wav"
# todo: move this writing process to audio.py
with open(fileName, 'wb') as f:
    f.write(response.content)

    f.close()

# play the file
audioInstance.playFile(fileName)
