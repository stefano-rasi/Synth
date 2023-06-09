import os
import sys
import time

import pprint
import argparse
import importlib

sys.path.insert(0, 'synth')

from midi_input import MidiInput
from audio_output import AudioOutput
from keyboard_input import KeyboardInput

parser = argparse.ArgumentParser(prog='synth')

parser.add_argument('path', nargs='?')

parser.add_argument('-s', '--sample_rate', type=int, default=44100)
parser.add_argument('-i', '--input_device', type=int)
parser.add_argument('-o', '--output_device', type=int)

parser.add_argument('-I', '--input_devices', action='store_true')
parser.add_argument('-O', '--output_devices', action='store_true')

args = parser.parse_args()

pp = pprint.PrettyPrinter()

if args.input_devices:
    pp.pprint(MidiInput.devices())

    quit()

if args.output_devices:
    pp.pprint(AudioOutput.devices())

    quit()

path = args.path

sample_rate = args.sample_rate
input_device = args.input_device
output_device = args.output_device

if args.input_device is not None:
    midi_input = MidiInput(args.input_device)
else:
    midi_input = KeyboardInput()

audio_output = AudioOutput(output_device, sample_rate)

mtime = os.path.getmtime(path)

name = path.strip('./') \
           .strip('.\\') \
           .strip('.py') \
           .replace('/', '.') \
           .replace('\\', '.')

module = importlib.import_module(name)

module.Sound(midi_input, audio_output, sample_rate)

audio_output.stream.start_stream()

while audio_output.stream.is_active():
    new_mtime = os.path.getmtime(path)

    if new_mtime != mtime:
        mtime = new_mtime

        audio_output.effects = []
        audio_output.sources = []

        importlib.reload(module)

        module.Sound(midi_input, audio_output, sample_rate)
    else:
        time.sleep(0.1)