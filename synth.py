import os
import sys
import time

import importlib

sys.path.insert(0, 'lib')

from audio_output import AudioOutput
from keyboard_input import KeyboardInput

SAMPLE_RATE = 44100

path = sys.argv[1]

mtime = os.path.getmtime(path)

if len(sys.argv) > 2:
    device = sys.argv[2]
else:
    device = 4

name = path.strip('.\\').strip('.py').replace('\\', '.')

module = importlib.import_module(name)

midi_input = KeyboardInput()

audio_output = AudioOutput(device)

module.Sound(midi_input, audio_output, SAMPLE_RATE)

audio_output.stream.start_stream()

while audio_output.stream.is_active():
    new_mtime = os.path.getmtime(path)

    if new_mtime != mtime:
        mtime = new_mtime

        audio_output.reset()

        importlib.reload(module)

        module.Sound(midi_input, audio_output, SAMPLE_RATE)
    else:
        time.sleep(0.1)
