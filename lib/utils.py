def power_to_amplitude(a, min=-100):
    db = a * (-min) + min

    return (10 ** (db / 20))