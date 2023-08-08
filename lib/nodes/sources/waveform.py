from nodes.waveform import WaveformNode
from nodes.envelope import EnvelopeNode

from sources.waveform import WaveformSource

class WaveformSourceNode:
    def __init__(self, tag, midi_input, audio_output):
        waveform_tag = tag.find('waveform')

        waveform_node = WaveformNode(waveform_tag)

        waveform = waveform_node.waveform

        if tag.find('envelope'):
            envelope_node = EnvelopeNode(tag.find('envelope'), audio_output.sample_rate)

            envelope = envelope_node.envelope
        else:
            envelope = None

        source = WaveformSource(waveform, audio_output.sample_rate, envelope)

        midi_input.sources.append(source)
        audio_output.sources.append(source)