from nodes.waveform import WaveformNode
from sources.waveform import WaveformSource

class WaveformSourceNode:
    def __init__(self, tag, midi_input, audio_output):
        waveform_tag = child.find('waveform')

        waveform_node = WaveformNode(waveform_tag)

        waveform = waveform_node.waveform

        source = WaveformSource(waveform, audio_outpu.sample_rate)

        audio_output.sources.append(source)