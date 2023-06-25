import sys
import time
import pprint

sys.path.insert(0, '')

from audio_output import AudioOutput

pp = pprint.PrettyPrinter(indent=1)

pp.pprint(AudioOutput.devices())