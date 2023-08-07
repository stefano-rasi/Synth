import yaml

from waveforms.harmonics import HarmonicsWaveform

class HarmonicsWaveformNode:
    def __init__(self, tag):
        harmonics_tag = tag.find('harmonics')

        harmonics = yaml.load(harmonics_tag.text)

        for h in harmonics.keys():
            harmonics[h] /= 100

        self.waveform = HarmonicsWaveform(harmonics)