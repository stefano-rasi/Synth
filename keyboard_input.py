from midi_input import MidiInput

from pynput.keyboard import Listener

class KeyboardInput:
    VELOCITY = 100

    NOTES = {
        'z': 0, 's': 1,
        'x': 2, 'd': 3,
        'c': 4,
        'v': 5, 'g': 6,
        'b': 7, 'h': 8,
        'n': 9, 'j': 10,
        'm': 11,
        ',': 12,

        'w': 12, '3': 13,
        'e': 14, '4': 15,
        'r': 16,
        't': 17, '6': 18,
        'y': 19, '7': 20,
        'u': 21, '8': 22,
        'i': 23,
        'o': 24
    }

    def __init__(self):
        self._events = []
        self._pressed = []

        listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

        listener.start()

    def midi_note(self, key):
        if hasattr(key, 'char') and key.char in self.NOTES:
            return 60 + self.NOTES[key.char]
        else:
            return None

    def on_press(self, key):
        note = self.midi_note(key)

        if note and key not in self._pressed:
            self._pressed.append(key)

            self._events.append({
                'note': note,
                'event': MidiInput.NOTE_ON,
                'velocity': self.VELOCITY
            })

    def on_release(self, key):
        note = self.midi_note(key)

        if note:
            if key in self._pressed:
                self._pressed.remove(key)

            self._events.append({
                'note': note,
                'event': MidiInput.NOTE_OFF,
                'velocity': self.VELOCITY
            })

    def events(self):
        events = self._events[:]

        self._events.clear()

        return events