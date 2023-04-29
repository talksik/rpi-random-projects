# rpi-random-projects

# Connection
ssh username@hostname.local -v
- the v will give verbose output

Use `arp -a` to see what the ip address and hostname is for the connected rpi.
Make sure that the arp connection is complete and not (incomplete)

Wait for connection. Sometimes can take some time.

# Setup for audio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip install pyaudio

https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT_Raspberry/#picovoice-with-respeaker-2-mic-pi-hat-and-raspberry-pi-zero-getting-started
- clone the repo and do the ./install.sh (use the higher kernel one in this repo itself
if the rpi is newer)

# Running things
Make sure python path is set to the root directory of the project. That ensures
that we can reuse modules/other directories such as our internal audio module.


Some programs have to be run from the project within the repo (such as voice-server)
while others can be run from the root directory of the project directly.
