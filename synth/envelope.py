import numpy as np

class EnvelopeFactory:
    def __init__(self, attack, decay=[], release=[]):
        self.decay = decay
        self.attack = attack
        self.release = release

    def build_envelope(self):
        return Envelope(self.attack, self.decay, self.release)

class Envelope:
    def __init__(self, attack=[], decay=[], release=[]):
        self.a = 0
        self.d = 0
        self.r = 0

        self.decay = np.array(decay)
        self.attack = np.array(attack)
        self.release = np.array(release)

        self.released = False

        self.last_decay = 1
        self.last_attack = 1

    def take(self, frame_count):
        if not self.released and self.a < len(self.attack):
            stop = self.a + frame_count
            start = self.a

            self.a += frame_count

            samples = self.attack.take(range(start, stop), mode='clip')

            self.last_attack = samples[-1]

            return samples
        elif not self.released and self.d < len(self.decay):
            stop = self.d + frame_count
            start = self.d

            self.d += frame_count

            samples = self.decay.take(range(start, stop), mode='clip')

            self.last_decay = samples[-1]

            return samples
        elif not self.released:
            if self.last_decay:
                samples = np.repeat(self.last_decay, frame_count)
            else:
                samples = np.repeat(self.last_attack, frame_count)

            return samples
        elif self.release.size:
            if self.r >= len(self.release):
                return False
            elif self.r + frame_count < len(self.release):
                stop = self.r + frame_count
                start = self.r

                self.r += frame_count

                samples = self.release[start:stop]

                if self.last_decay:
                    return self.last_decay * samples
                else:
                    return self.last_attack * samples
            else:
                samples = np.zeros(frame_count)

                stop = min(self.r + frame_count, len(self.release))
                start = self.r

                samples[:stop-start] = self.release[start:stop]

                self.r += frame_count

                if self.last_decay:
                    return self.last_decay * samples
                else:
                    return self.last_attack * samples
        else:
            return False