import numpy as np

from midi_input import MidiInput

from utils import midi_to_frequency

class WaveformSource:
    def __init__(self, waveform, midi_input, envelope=None):
        self.notes = []

        self.waveform = waveform

        self.envelope = envelope

        self.midi_input = midi_input

    def samples(self, frame_count):
        events = self.midi_input.events()

        for event in events:
            if event['event'] == MidiInput.NOTE_ON:
                note = event['note']

                pitch = midi_to_frequency(note)

                if self.envelope:
                    envelope = self.envelope.build_envelope()
                else:
                    envelope = None

                waveform = self.waveform.waveform(pitch, self.sample_rate)

                self.notes.append({
                    't': 0,
                    'note': note,
                    'pitch': pitch,
                    'envelope': envelope,
                    'waveform': waveform
                })
            elif event['event'] == MidiInput.NOTE_OFF:
                notes = [n for n in self.notes if n['note'] == event['note']]

                if notes:
                    for note in notes:
                        note['envelope'].released = True
                else:
                    self.notes = [n for n in self.notes if not n['note'] == event['note']]

        samples = np.zeros(frame_count)

        for note in self.notes[:]:
            waveform_range = range(note['t'], note['t'] + frame_count)

            waveform_samples = note['waveform'].take(waveform_range, mode='wrap')

            if note['envelope']:
                envelope_samples = note['envelope'].take(frame_count)

                if envelope_samples is False:
                    self.notes.remove(note)
                else:
                    samples += envelope_samples * waveform_samples
            else:
                samples += waveform_samples

            note['t'] += frame_count

        return samples