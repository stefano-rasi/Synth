import numpy as np

class HarmonicsWaveform:
    def __init__(self, harmonics):
        self.harmonics = harmonics

    def waveform(self, pitch, sample_rate):
        harmonics = np.insert(self.harmonics, 0, 0)
        harmonics = harmonics[:int(round(sample_rate/2 / pitch))]

        wavelength = int(round(sample_rate/pitch * 4))

        fft = np.zeros(wavelength)

        indexes = 8 * np.arange(len(harmonics), dtype=int)

        fft[indexes] = harmonics

        waveform = scipy.fftpack.irfft(fft) * wavelength/2

        return waveform