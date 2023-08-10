from nodes.waveforms.note import NoteWaveformNode
from nodes.waveforms.noise import NoiseWaveformNode
from nodes.waveforms.formant import FormantWaveformNode
from nodes.waveforms.harmonics import HarmonicsWaveformNode

class WaveformNode:
    def __init__(self, tag, sample_rate):
        child = tag.find()

        if child.name == 'note-waveform':
            waveform_node = NoteWaveformNode(child, sample_rate)
        elif child.name == 'noise-waveform':
            waveform_node = NoiseWaveformNode(child, sample_rate)
        elif child.name == 'formant-waveform':
            waveform_node = FormantWaveformNode(child, sample_rate)
        elif child.name == 'harmonics-waveform':
            waveform_node = HarmonicsWaveformNode(child)

        self.waveform = waveform_node.waveform