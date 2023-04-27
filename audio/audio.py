# this is a library to easily record and play audio

import pyaudio
import wave


RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 1  # refer to input device id
CHUNK = 1024
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
            start=False,
            stream_callback=self.readCallback,)

    def readCallback(self, out_data, frame_count, time_info, status):
        self.frames.append(out_data)
        # If len(data) is less than requested frame_count, PyAudio automatically
        # assumes the stream is finished, and the stream stops.
        return (out_data, pyaudio.paContinue)

    def isRecording(self):
        return self.recordStream.is_active()

    def startRecord(self):
        print("* recording stream started")
        self.recordStream.start_stream()
        self.frames = []

    def stopRecord(self, play=True, save=False):
        print("* done recording")
        self.recordStream.stop_stream()

        if save:
            self._saveFile()
        if play:
            self._playFrames()

        self.frames = []

    def _saveFile(self):
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(RESPEAKER_CHANNELS)
        wf.setsampwidth(self.pyaudio.get_sample_size(
            self.pyaudio.get_format_from_width(RESPEAKER_WIDTH)))
        wf.setframerate(RESPEAKER_RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def _playFrames(self):
        print("* playing recorded audio")
        print(len(self.frames))

        playbackStream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            rate=RESPEAKER_RATE,
            output=True,
            output_device_index=RESPEAKER_INDEX)

        # loop through self.frames and play audio
        for frame in self.frames:
            playbackStream.write(frame)

        print("* done playing recorded audio")

        # cleanup stuff
        playbackStream.stop_stream()

    def terminate(self):
        self.pyaudio.terminate()
