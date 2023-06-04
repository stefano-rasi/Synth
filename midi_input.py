import pygame.midi

class MidiInput:
    EVENTS = 32

    def __init__(self, device):
        pygame.midi.init()

        midi_input = pygame.midi.Input(device)

    def events(self):
        events = []

        midi_events = midi_input.read(EVENTS)

        for midi_event in midi_events:
            note = midi_event[0][1]
            event = midi_event[0][0]
            velocity = midi_event[0][2]

            events.append({
                'note': note,
                'event': event,
                'velocity': velocity
            })

        return events