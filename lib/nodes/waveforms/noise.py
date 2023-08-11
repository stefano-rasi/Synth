from nodes.formant import FormantNode

from waveforms.noise import NoiseWaveform

class NoiseWaveformNode:
    def __init__(self, tag, sample_rate):
        formant_tag = tag.find('formant')

        formant_node = FormantNode(formant_tag)

        formant = formant_node.formant

        if tag.has_attr('lazy'):
            if tag['lazy'] == 'false':
                lazy = False
            else:
                lazy = True
        else:
            lazy = True

        self.waveform = NoiseWaveform(formant, sample_rate, lazy=lazy)