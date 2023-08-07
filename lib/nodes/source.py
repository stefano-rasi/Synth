from nodes.sources.waveform import WaveformSourceNode

class SourceNode:
    def __init__(self, tag, midi_input, audio_output):
        child = next(tag.children, None)

        if child.name == 'waveform-source':
            WaveformSourceNode(child, midi_input, audio_output)