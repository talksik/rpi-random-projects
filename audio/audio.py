# this is a library to easily record and play audio

import pyaudio
import wave


RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 1  # refer to input device id
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


class Audio:
    def __init__(self):
        self.frames = []
        self.pyaudio = pyaudio.PyAudio()
        self.recordStream = self.pyaudio.open(
            rate=RESPEAKER_RATE,
            format=self.pyaudio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            input_device_index=RESPEAKER_INDEX,
            start=False,)

    def startRecord(self):
        self.frames = []
        print("* recording")
        for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
            data = self.recordStream.read(CHUNK)
            print("read a chunk")
            self.frames.append(data)

    def stopRecord(self, play=True, save=False):
        print("* done recording")
        print(self.frames)
        self.recordStream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

        if save:
            self._saveFile()

    def _saveFile(self):
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(RESPEAKER_CHANNELS)
        wf.setsampwidth(self.pyaudio.get_sample_size(
            self.pyaudio.get_format_from_width(RESPEAKER_WIDTH)))
        wf.setframerate(RESPEAKER_RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def playFrames(self):
        self.playbackStream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            rate=RESPEAKER_RATE,
            output=True,
            output_device_index=RESPEAKER_INDEX)

        # loop through self.frames and play audio
        for frame in self.frames:
            self.playbackStream.write(frame)

        # cleanup stuff
        self.playbackStream.close()
        self.pyaudio.terminate()
