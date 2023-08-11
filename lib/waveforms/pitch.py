import math

from utils.audio import power_to_amplitude

class PitchWaveform:
    def __init__(self, waveforms):
        self.waveforms = waveforms

    def waveform(self, pitch, sample_rate):
        waveform_stop = None
        waveform_start = None

        for waveform in self.waveforms:
            if pitch <= waveform['pitch']:
                if not waveform_stop:
                    waveform_stop = waveform
            if pitch >= waveform['pitch']:
                waveform_start = waveform

        if not waveform_stop:
            waveform_stop = self.waveforms[-1]

        if not waveform_start:
            waveform_start = self.waveforms[0]

        pitch_stop = waveform_stop['pitch']
        pitch_start = waveform_start['pitch']

        if pitch >= pitch_stop:
            stop_amplitude = 1
            start_amplitude = 0
        elif pitch <= pitch_start:
            stop_amplitude = 0
            start_amplitude = 1
        else:
            pitch_log = math.log2(pitch)

            pitch_stop_log = math.log2(pitch_stop)
            pitch_start_log = math.log2(pitch_start)

            start_power = (pitch_stop_log - pitch_log) / (pitch_stop_log - pitch_start_log)

            stop_power = 1 - start_power

            stop_amplitude = power_to_amplitude(stop_power, -18)
            start_amplitude = power_to_amplitude(start_power, -18)

        stop_waveform = waveform_stop['waveform'].waveform(pitch, sample_rate)
        start_waveform = waveform_start['waveform'].waveform(pitch, sample_rate)

        waveform = start_amplitude * start_waveform + stop_amplitude * stop_waveform

        return waveform