import pygame.midi

class MidiInput:
    EVENTS = 32

    NOTE_ON = 0x9C
    NOTE_OFF = 0x8C

    def devices():
        pygame.midi.init()

        devices = []

        for i in range(pygame.midi.get_count()):
            device = pygame.midi.get_device_info(i)

            if device[2] == 1:
                devices.append(device)

        pygame.midi.quit()

        return devices

    def __init__(self, device):
        pygame.midi.init()

        self.midi_input = pygame.midi.Input(device)

    def events(self):
        events = []

        midi_events = self.midi_input.read(self.EVENTS)

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

    def midi_to_frequency(midi_note):
        return 440 * pow(2, (midi_note - 69) / 12)