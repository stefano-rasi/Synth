from nodes.formant import FormantNode
from waveforms.formant import FormantWaveform

class FormantWaveformNode:
    def __init__(self, tag, sample_rate):
        formant_tag = tag.find('formant')

        formant_node = FormantNode(formant_tag)

        formant = formant_node.formant

        self.waveform = FormantWaveform(formant, sample_rate)