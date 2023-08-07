from nodes.source import SourceNode

class SoundNode:
    def __init__(self, tag, midi_input, audio_output):
        for source_tag in tag.find_all('source'):
            SourceNode(source_tag, midi_input, audio_output)