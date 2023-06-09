import scipy

import numpy as np

class NoiseWaveform:
    def __init__(self, formant, sample_rate, lazy=True):
        self.lazy = lazy

        self.formant = formant.formant(sample_rate)

        self.complex_formant = np.array(self.formant, dtype='complex')

        if not lazy:
            random_angles = np.random.rand(len(self.formant)) * (2 * np.pi)

            fft_angles = (np.cos(random_angles) + 1j * np.sin(random_angles))

            half_fft = self.complex_formant * fft_angles

            noise_fft = np.concatenate((half_fft, np.flipud(np.conj(half_fft[1:]))))

            self._waveform = scipy.fftpack.ifft(noise_fft).real * (len(self.formant) / 2)

    def waveform(self, pitch, sample_rate):
        if self.lazy:
            random_angles = np.random.rand(len(self.formant)) * (2 * np.pi)

            fft_angles = (np.cos(random_angles) + 1j * np.sin(random_angles))

            half_fft = self.complex_formant * fft_angles

            noise_fft = np.concatenate((half_fft, np.flipud(np.conj(half_fft[1:]))))

            waveform = scipy.fftpack.ifft(noise_fft).real * (len(self.formant) / 2)

            return waveform
        else:
            return self._waveform