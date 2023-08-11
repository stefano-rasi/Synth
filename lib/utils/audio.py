def db_to_amplitude(db):
    return (10 ** (db / 20))

def power_to_amplitude(samples, min_db=-100):
    db = samples * (-min_db) + min_db

    return db_to_amplitude(db)