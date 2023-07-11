import math
import scipy

import numpy as np

class FormantWaveform:
    SCALE = 4

    def __init__(self, formant, sample_rate, harmonics=None):
        self.harmonics = harmonics

        self.formant = formant.formant(sample_rate)

    def waveform(self, pitch, sample_rate):
        max_freq = int(round((sample_rate / pitch / 2))) - 1

        if self.harmonics is None:
            harmonics = np.repeat(1, max_freq)
        else:
            harmonics = self.harmonics[:max_freq]

        wavelength = int(round(sample_rate / pitch * self.SCALE))

        harmonics_fft = np.zeros(wavelength)

        harmonics_indexes = 2 * self.SCALE * np.arange(len(harmonics), dtype=int)

        harmonics_frequencies = pitch * np.arange(1, len(harmonics) + 1)

        harmonics_fft[harmonics_indexes] = self.formant[harmonics_frequencies.astype(int)] * harmonics

        waveform = scipy.fftpack.irfft(harmonics_fft) * (wavelength / 2)

        return waveform