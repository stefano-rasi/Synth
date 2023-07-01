def midi_to_frequency(note):
    return 440 * pow(2, (note - 69) / 12)

def power_to_amplitude(samples, min=-100):
    decibels = samples * (-min) + min

    return (10 ** (decibels / 20))