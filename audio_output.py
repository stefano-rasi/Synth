import pyaudio

import numpy as np

class AudioOutput:
    def devices():
        p = pyaudio.PyAudio()

        devices = []

        for i in range(p.get_device_count()):
            device = p.get_device_info_by_index(i)

            if device['maxOutputChannels'] > 0:
                devices.append(device)

        p.terminate()

        return devices

    def __init__(self, device, sample_rate=44100):
        self.sources = []

        p = pyaudio.PyAudio()

        stream = p.open(
            rate=sample_rate,
            output=True,
            format=pyaudio.paFloat32,
            channels=1,
            stream_callback=self.callback,
            output_device_index=device,
        )

        stream.start_stream()

    def add_source(self, source):
        self.sources.append(source)

    def callback(self, in_data, frame_count, time_info, status):
        samples = np.zeros(frame_count)

        for source in self.sources:
            samples += source.samples(frame_count)

        return (samples, pyaudio.paContinue)