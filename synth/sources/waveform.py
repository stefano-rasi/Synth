import numpy as np

from utils import midi_to_pitch

from midi_input import MidiInput

class WaveformSource:
    def __init__(self, waveform, midi_input, envelope_factory=None, velocity_curve=None):
        self.notes = []

        self.waveform = waveform

        self.midi_input = midi_input

        self.envelope_factory = envelope_factory

        if velocity_curve:
            self.velocity_curve = velocity_curve.interpolate(128)
        else:
            self.velocity_curve = None

    def samples(self, frame_count):
        events = self.midi_input.events()

        for event in events:
            if event['event'] == MidiInput.NOTE_ON:
                note = event['note']

                pitch = midi_to_pitch(note)

                velocity = event['velocity']

                if self.velocity_curve is not None:
                    amplitude = self.velocity_curve[velocity]
                else:
                    amplitude = velocity / 127

                if self.envelope_factory:
                    envelope = self.envelope_factory.build_envelope()
                else:
                    envelope = None

                waveform = self.waveform.waveform(pitch, self.sample_rate)

                self.notes.append({
                    't': 0,
                    'note': note,
                    'pitch': pitch,
                    'envelope': envelope,
                    'waveform': waveform,
                    'amplitude': amplitude
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
            amplitude = note['amplitude']

            waveform_range = range(note['t'], note['t'] + frame_count)

            waveform_samples = note['waveform'].take(waveform_range, mode='wrap')

            if note['envelope']:
                envelope = note['envelope'].take(frame_count)

                if envelope is False:
                    self.notes.remove(note)
                else:
                    samples += amplitude * envelope * waveform_samples
            else:
                samples += amplitude * waveform_samples

            note['t'] += frame_count

        return samples