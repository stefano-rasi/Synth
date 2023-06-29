import numpy as np

class EnvelopeFactory:
    def __init__(self, attack, release=[]):
        self.attack = attack
        self.release = release

    def build_envelope(self):
        return Envelope(self.attack, self.release)

class Envelope:
    def __init__(self, attack, release=[]):
        self.a = 0
        self.r = 0

        self.attack = np.array(attack)
        self.release = np.array(release)

        self.released = False

        self.last_attack = 0

    def take(self, frame_count):
        if not self.released and self.a < len(self.attack):
            attack_start = self.a
            attack_stop = self.a + frame_count

            if self.released and (attack_stop >= len(self.attack)):
                samples = np.empty(frame_count)

                attack_stop = len(self.attack)

                attack_length = attack_stop - attack_start

                samples[:attack_length] = self.attack[attack_start:attack_stop]

                self.a += attack_length

                if self.release.size:
                    release_length = frame_count - attack_length

                    release_start = self.r
                    release_stop = self.r + release_length

                    samples[attack_length:] = self.release[release_start:release_stop]

                    self.r += release_length

                self.last_attack = samples[-1]

                return samples
            else:
                self.a += frame_count

                samples = self.attack.take(range(attack_start, attack_stop), mode='clip')

                self.last_attack = samples[-1]

                return samples
        elif not self.released:
            samples = np.repeat(self.attack[-1], frame_count)

            self.last_attack = samples[-1]

            return samples
        elif self.release.size:
            if self.r >= len(self.release):
                return False
            elif self.r + frame_count < len(self.release):
                release_start = self.r
                release_stop = self.r + frame_count

                self.r += frame_count

                release_samples = self.release[release_start:release_stop]

                return self.last_attack * release_samples
            else:
                release_samples = np.zeros(frame_count)

                release_start = self.r
                release_stop = min(self.r + frame_count, len(self.release))

                release_samples[:release_stop-release_start] = self.release[release_start:release_stop]

                self.r += frame_count

                return self.last_attack * release_samples
        else:
            return False