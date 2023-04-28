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
        self.recordStream = None
        self.playbackStream = None
        self._isRecording = False

    def readCallback(self, out_data, frame_count, time_info, status):
        self.frames.append(out_data)
        return (out_data, pyaudio.paContinue)

    def isRecording(self):
        return self._isRecording

    def startRecord(self):
        print("* recording stream started")
        self.frames = []
        self.recordStream = self.pyaudio.open(
            rate=RESPEAKER_RATE,
            format=self.pyaudio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            input_device_index=RESPEAKER_INDEX,
            start=False,
            frames_per_buffer=CHUNK,
            stream_callback=self.readCallback,
        )
        self.recordStream.start_stream()
        self._isRecording = True

    def stopRecord(self, play=True, save=False):
        print("* done recording")
        self.recordStream.stop_stream()
        self.recordStream.close()
        self._isRecording = False

        savedFileName = None
        if save:
            savedFileName = self._saveFile()
        if play:
            self._playFrames()

        self.frames = []

        return savedFileName if save else self.frames

    def _saveFile(self):
        wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
        wf.setnchannels(RESPEAKER_CHANNELS)
        wf.setsampwidth(
            self.pyaudio.get_sample_size(
                self.pyaudio.get_format_from_width(RESPEAKER_WIDTH)
            )
        )
        wf.setframerate(RESPEAKER_RATE)
        wf.writeframes(b"".join(self.frames))
        wf.close()
        return WAVE_OUTPUT_FILENAME

    def _playFrames(self):
        print("* playing recorded audio")
        print(len(self.frames))

        self.playbackStream = self.pyaudio.open(
            format=self.pyaudio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            rate=RESPEAKER_RATE,
            output=True,
            output_device_index=RESPEAKER_INDEX,
        )

        # loop through self.frames and play audio
        for frame in self.frames:
            self.playbackStream.write(frame)

        print("* done playing recorded audio")

        # cleanup stuff
        self.playbackStream.stop_stream()
        self.playbackStream.close()

    def terminate(self):
        self.pyaudio.terminate()
