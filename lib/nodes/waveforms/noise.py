from nodes.formant import FormantNode

from waveforms.noise import NoiseWaveform

class NoiseWaveformNode:
    def __init__(self, tag, sample_rate):
        formant_tag = tag.find('formant')

        formant_node = FormantNode(formant_tag)

        formant = formant_node.formant

        self.waveform = NoiseWaveform(formant, sample_rate, lazy=False)