import scipy
import numpy as np

class ConvolutionReverb:
    LIMIT = 60000

    def __init__(self, file):
        wavfile = scipy.io.wavfile.read(file)

        mono_samples = np.array(wavfile[1])[:,0]

        impulse = mono_samples[:self.LIMIT].astype(np.float32) / 2**15

        self.window = np.zeros(len(impulse))

        self.impulse_fft = scipy.fft.rfft(impulse)

        self.impulse_fft_amax = np.amax(self.impulse_fft)

    def process(self, samples):
        self.window = np.roll(self.window, -len(samples))

        self.window[-len(samples):] = samples

        window_fft = scipy.fft.rfft(self.window)

        convolution = scipy.fft.irfft(window_fft * self.impulse_fft / self.impulse_fft_amax)

        return convolution[-len(samples):]