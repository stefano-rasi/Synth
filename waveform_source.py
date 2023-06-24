class WaveformSource:
    def __init__(self, midi_input, audio_output, waveform, envelope):
        self.notes = []

        self.waveform = waveform
        self.enevelope = envelope
        self.midi_input = midi_input
        self.audio_output = audio_output