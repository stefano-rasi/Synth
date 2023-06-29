import scipy

import numpy as np

class HarmonicsWaveform:
    def __init__(self, harmonics):
        self.harmonics = harmonics

    def samples(self, pitch, sample_rate):
        harmonics = np.insert(self.harmonics, 0, 0)
        harmonics = harmonics[:int(round(sample_rate/2 / pitch))]

        wavelength = int(round(sample_rate/pitch * 4))

        harmonics_fft = np.zeros(wavelength)

        harmonics_indexes = 8 * np.arange(len(harmonics), dtype=int)

        harmonics_fft[harmonics_indexes] = harmonics

        samples = scipy.fft.irfft(harmonics_fft) * wavelength/2

        return samples