class WaveformSource:
    def __init__(self, midi_input, audio_output, waveform, envelope):
        self.notes = []

        self.output = output
        self.waveform = waveform
        self.enevelope = envelope
        self.midi_input = midi_input

    def samples(self, n):
        events = self.midi_input.events()

        for event in events:
            if event.event == "NOTE_ON":
                self.waveform.waveform(pitch, self.output.sample_rate)

    class Note:
        def __init__(midi_note, velocity, waveform):