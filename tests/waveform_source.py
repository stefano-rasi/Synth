import sys
import time

sys.path.insert(0, '')

from audio_output import AudioOutput
from keyboard_input import KeyboardInput
from waveform_source import WaveformSource
from harmonics_waveform import HarmonicsWaveform

DEVICE = 4

input = KeyboardInput()
output = AudioOutput(DEVICE)

waveform = HarmonicsWaveform([0.1, 0.04, 0.02])

source = WaveformSource(waveform, input, output)

while output.is_active():
    time.sleep(0.1)