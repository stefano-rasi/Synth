import sys
import pprint

sys.path.insert(0, '')

from midi_input import MidiInput

pp = pprint.PrettyPrinter(indent=1)

pp.pprint(MidiInput.devices())