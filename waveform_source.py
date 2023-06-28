import numpy as np

from midi_input import MidiInput

class WaveformSource:
    def __init__(self, waveform, midi_input, envelope=None):
        self.notes = []

        self.waveform = waveform

        self.midi_input = midi_input

    def samples(self, frame_count):
        events = self.midi_input.events()

        for event in events:
            if event['event'] == MidiInput.NOTE_ON:
                note = event['note']

                pitch = MidiInput.midi_to_frequency(note)

                waveform = self.waveform.samples(pitch, self.sample_rate)

                self.notes.append({
                    't': 0,
                    'note': note,
                    'pitch': pitch,
                    'waveform': waveform
                })
            elif event['event'] == MidiInput.NOTE_OFF:
                note = event['note']

                self.notes = [n for n in self.notes if not n['note'] == note]

        samples = np.zeros(frame_count)

        for note in self.notes:
            waveform_range = range(note['t'], note['t'] + frame_count)

            samples += note['waveform'].take(waveform_range, mode='wrap')

            note['t'] += frame_count

        return samples