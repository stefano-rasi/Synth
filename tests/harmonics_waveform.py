import sys
import time
import pyaudio

import numpy as np

from matplotlib import pyplot as plt

sys.path.insert(0, '')

from harmonics_waveform import HarmonicsWaveform

DEVICE = 4
SAMPLE_RATE = 44100

harmonics_waveform = HarmonicsWaveform([ 0.5, 0.3, 0.4 ])

waveform = harmonics_waveform.waveform(220, SAMPLE_RATE)

def callback(in_data, frame_count, time_info, status):
    t = callback.t

    samples_range = range(t, t + frame_count)

    samples = waveform.take(samples_range, mode='wrap')

    callback.t += frame_count

    return (samples.astype(np.float32), pyaudio.paContinue)

callback.t = 0

p = pyaudio.PyAudio()

stream = p.open(
    rate=SAMPLE_RATE,
    output=True,
    format=pyaudio.paFloat32,
    channels=1,
    stream_callback=callback,
    output_device_index=DEVICE,
)

while True:
    time.sleep(1)