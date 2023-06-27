import scipy
import numpy as np

class ConvolutionReverb:
    LIMIT = 45000

    def __init__(self, file):
        wavfile = scipy.io.wavfile.read(file)

        samples = np.array(wavfile[1])[:,0]

        samples = samples[:self.LIMIT]

        self.impulse = samples.astype(np.float32) / 2**15

        self.window = np.zeros(len(self.impulse))

    def process(self, samples):
        self.window = np.roll(self.window, -len(samples))

        self.window[-len(samples):] = samples

        window_fft = scipy.fft.rfft(self.window)
        impulse_fft = scipy.fft.rfft(self.impulse)

        convolution = scipy.fft.irfft(window_fft * impulse_fft / np.amax(impulse_fft))

        return convolution[-len(samples):]