import time
import threading

import pygame.midi

class MidiInput:
    EVENTS = 32

    NOTE_ON = 144
    NOTE_OFF = 128

    def devices():
        pygame.midi.init()

        devices = []

        for i in range(pygame.midi.get_count()):
            device = pygame.midi.get_device_info(i)

            if device[2] == 1:
                devices.append([i, device[1]])

        pygame.midi.quit()

        return devices

    def __init__(self, device):
        self.sources = []

        pygame.midi.init()

        self.midi_input = pygame.midi.Input(device)

        threading.Thread(target=self.listener, daemon=True).start()

    def listener(self):
        while True:
            events = []

            midi_events = self.midi_input.read(self.EVENTS)

            for midi_event in midi_events:
                note = midi_event[0][1]
                event = midi_event[0][0]
                velocity = midi_event[0][2]

                if event == self.NOTE_ON and velocity == 0:
                    event = self.NOTE_OFF

                events.append({
                    'note': note,
                    'event': event,
                    'velocity': velocity
                })

            for source in self.sources:
                source.events += events

            time.sleep(0.01)