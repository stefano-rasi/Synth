import math

from utils import power_to_amplitude

class InterpolationWaveform:
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
                if not waveform_start:
                    waveform_start = waveform

        pitch_log = math.log2(pitch)

        pitch_stop = waveform_stop['pitch']
        pitch_start = waveform_start['pitch']

        pitch_stop_log = math.log2(pitch_stop)
        pitch_start_log = math.log2(pitch_start)

        stop_power = (pitch_stop_log - pitch_log) / (pitch_stop_log - pitch_start_log)
        start_power = 1 - stop_power

        if stop_power > start_power:
            stop_amplitude = power_to_amplitude(stop_power)
            start_amplitude = 1 - stop_amplitude
        else:
            start_amplitude = power_to_amplitude(start_power)
            stop_amplitude = 1 - start_amplitude

        stop_waveform = waveform_stop['waveform'].waveform(pitch, sample_rate)
        start_waveform = waveform_start['waveform'].waveform(pitch, sample_rate)

        waveform = start_amplitude * start_waveform + stop_amplitude * stop_waveform

        return waveform