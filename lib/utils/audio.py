def power_to_amplitude(samples, min_db=-60):
    db = samples * (-min_db) + min_db

    return (10 ** (db / 20))