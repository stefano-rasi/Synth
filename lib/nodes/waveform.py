from nodes.waveforms.harmonics import HarmonicsWaveformNode

class WaveformNode:
    def __init__(self, tag):
        child = next(tag.children, None)

        if child.name == 'harmonics-waveform':
            waveform_node = HarmonicsWaveformNode(child)

        self.waveform = waveform_node.waveform