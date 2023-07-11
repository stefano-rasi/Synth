import numpy as np

from utils import midi_to_pitch

from midi_input import MidiInput

class WaveformSource:
    def __init__(self, waveform, sample_rate, envelope=None, velocity=None):
        self.notes = []
        self.events = []

        self.waveform = waveform
        self.envelope = envelope

        self.sample_rate = sample_rate

        if velocity:
            self.velocity = velocity.interpolate(128)
        else:
            self.velocity = None

    def samples(self, frame_count):
        for event in self.events:
            if event['event'] == MidiInput.NOTE_ON:
                note = event['note']

                pitch = midi_to_pitch(note)

                velocity = event['velocity']

                if self.velocity is not None:
                    amplitude = self.velocity[velocity]
                else:
                    amplitude = velocity / 127

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
                    'waveform': waveform,
                    'amplitude': amplitude
                })
            elif event['event'] == MidiInput.NOTE_OFF:
                notes = [n for n in self.notes if n['note'] == event['note']]

                for note in notes:
                    if note['envelope']:
                        note['envelope'].released = True
                    else:
                        self.notes = [n for n in self.notes if not n['note'] == event['note']]

        self.events.clear()

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