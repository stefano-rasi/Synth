import scipy

import numpy as np

class Formant:
    def __init__(self, curve, min_freq=20, max_freq=20000, log=False):
        self.log = log

        self.curve = curve

        self.min_freq = min_freq
        self.max_freq = max_freq

    def formant(self, sample_rate):
        ys = self.curve

        xs = np.linspace(0, 1, len(self.curve))

        min_freq = self.min_freq
        max_freq = self.max_freq

        if self.log:
            min_freq_log = np.log2(min_freq)

            freq_range = np.log2(max_freq) - np.log2(min_freq)

            freq_xs = np.power(2, xs * freq_range + min_freq_log) / max_freq
        else:
            freq_range = max_freq - min_freq

            freq_xs = (xs * freq_range + min_freq) / max_freq

        interpolate = scipy.interpolate.interp1d(freq_xs, ys, fill_value='extrapolate')

        formant = interpolate(np.linspace(0, 1, int(round(sample_rate / 2))))

        return formant