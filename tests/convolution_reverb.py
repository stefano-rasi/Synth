import sys

sys.path.insert(0, '')

from audio_output import AudioOutput
from keyboard_input import KeyboardInput
from waveform_source import WaveformSource
from harmonics_waveform import HarmonicsWaveform
from convolution_reverb import ConvolutionReverb

DEVICE = 4

input = KeyboardInput()

output = AudioOutput(DEVICE)

waveform = HarmonicsWaveform([0.4, 0.16, 0.08])

source = WaveformSource(waveform, input, output)

effect = ConvolutionReverb('reverb/echo_hall.wav')

output.add_effect(effect)

output.start()