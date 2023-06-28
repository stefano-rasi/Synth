import scipy
import numpy as np

class ConvolutionReverb:
    LIMIT = 60000

    def __init__(self, file):
        wavfile = scipy.io.wavfile.read(file)

        mono_samples = np.array(wavfile[1])[:,0]

        length = min(self.LIMIT, len(mono_samples))

        impulse = mono_samples[:length].astype(np.float32) / 2**15

        self.window = np.zeros(len(impulse))

        self.impulse_fft = scipy.fft.rfft(impulse)

        self.impulse_fft_amax = np.amax(self.impulse_fft)

    def process(self, samples):
        self.window = np.roll(self.window, -len(samples))

        self.window[-len(samples):] = samples

        window_fft = scipy.fft.rfft(self.window)

        convolution_fft = window_fft * self.impulse_fft / self.impulse_fft_amax

        convolution = scipy.fft.irfft(convolution_fft)

        return convolution[-len(samples):]