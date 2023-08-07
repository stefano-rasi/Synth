MIDI_NOTES = {
    'C': 0, 'D': 2, 'E': 4,
    'F': 5, 'G': 7, 'A': 9, 'B': 11
}

def note_to_midi(name):
    note = name[0]
    octave = int(name[1])

    return 12 * (octave + 1) + MIDI_NOTES[note]

def note_to_pitch(name):
    return midi_to_pitch(note_to_midi(name))

def midi_to_pitch(note):
    return 440 * pow(2, (note - 69) / 12)

def power_to_amplitude(samples, min_db=-60):
    db = samples * (-min_db) + min_db

    return (10 ** (db / 20))