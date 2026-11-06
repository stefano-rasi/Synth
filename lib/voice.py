import numpy as np

class Voice:
    def __init__(self, waveform, envelope, amplitude=1, length=None):
        self.t = 0

        self.waveform = waveform

        self.envelope = envelope

        self.amplitude = amplitude

        self.length = length

    def get_samples(self, sample_count):
        if self.length is not None and self.t >= self.length:
            self.envelope.release()

        envelope = self.envelope.take(sample_count)

        if envelope is None:
            return None

        samples = self.waveform.take(range(self.t, self.t + sample_count), mode='wrap')

        self.t += sample_count

        return self.amplitude * envelope * samples

    def release(self):
        self.envelope.release()

class Sample:
    def __init__(self, samples, amplitude=1):
        self.t = 0

        self.samples = samples

        self.amplitude = amplitude

    def get_samples(self, sample_count):
        if self.t >= len(self.samples):
            return None

        samples = np.zeros(sample_count)

        chunk = self.samples[self.t:self.t + sample_count]

        samples[:len(chunk)] = chunk

        self.t += sample_count

        return self.amplitude * samples
