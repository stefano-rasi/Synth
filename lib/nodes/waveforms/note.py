from utils.midi import note_to_pitch

from waveforms.pitch import PitchWaveform

class NoteWaveformNode:
    def __init__(self, tag, sample_rate):
        from nodes.waveform import WaveformNode

        waveforms = []

        for note_tag in tag.find_all('note'):
            note = note_tag['name']

            pitch = note_to_pitch(note)

            child = note_tag.find()

            waveform_node = WaveformNode(child, sample_rate)

            waveform = waveform_node.waveform

            waveforms.append({
                'pitch': pitch,
                'waveform': waveform
            })

        self.waveform = PitchWaveform(waveforms)