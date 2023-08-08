import yaml

import numpy as np

from utils.audio import power_to_amplitude

from waveforms.harmonics import HarmonicsWaveform

class HarmonicsWaveformNode:
    def __init__(self, tag):
        harmonics_tag = tag.find('harmonics')

        harmonics = yaml.safe_load(harmonics_tag.text)

        harmonics_array = np.zeros(list(harmonics)[-1])

        if harmonics_tag.has_attr('max'):
            harmonics_max = float(harmonics_tag['max'])
        else:
            harmonics_max = 1

        for h in harmonics.keys():
            harmonics_array[h-1] = power_to_amplitude(harmonics[h] / harmonics_max)

        self.waveform = HarmonicsWaveform(harmonics_array)