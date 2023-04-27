import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    currDeviceInfo = p.get_device_info_by_host_api_device_index(0, i)
    if (currDeviceInfo.get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", currDeviceInfo.get('name'))
    else:
        print("Output Device id ", i, " - ", currDeviceInfo.get('name'))
