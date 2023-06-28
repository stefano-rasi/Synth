import time
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

    def __init__(self, device_index, sample_rate=44100):
        self.sources = []
        self.effects = []

        self.sample_rate = sample_rate

        p = pyaudio.PyAudio()

        self.stream = p.open(
            rate=sample_rate,
            output=True,
            format=pyaudio.paFloat32,
            channels=1,
            stream_callback=self.callback,
            output_device_index=device_index,
        )

    def add_source(self, source):
        self.sources.append(source)

        source.sample_rate = self.sample_rate
    
    def add_effect(self, effect):
        self.effects.append(effect)

    def callback(self, in_data, frame_count, time_info, status):
        samples = np.zeros(frame_count)

        for source in self.sources:
            samples += source.samples(frame_count)

        for effect in self.effects:
            samples = effect.process(samples)

        return (samples.clip(-1, 1).astype(np.float32), pyaudio.paContinue)

    def start(self):
        self.stream.start_stream()

        while self.stream.is_active():
            time.sleep(0.1)