```mermaid
---
title: Input
---
classDiagram
  class MidiInput {
    + new(device)
    + add_note_on_listener(listener)
    + add_note_off_listener(listener)
  }
  class KeyboardInput {
    + new()
    + add_note_on_listener(listener)
    + add_note_off_listener(listener)
  }
```

```mermaid
---
title: Waveforms
---
classDiagram
  class HarmonicsWaveform {
    + new(harmonics)
    + get_waveform(sample_rate, pitch)
  }
  class FormantWaveform {
    + new(formant)
    + get_waveform(sample_rate, pitch)
  }
  class NoiseWaveform {
    + new(formant)
    + get_waveform(sample_rate)
  }
```

```mermaid
---
title: Envelopes
---
classDiagram
  class AttackReleaseEnvelope {
    + new(attack, release)
    + release()
    + get_values(n)
  }
```

```mermaid
---
title: Sources
---
classDiagram
  class WaveformSource {
    + new(waveform, envelope)
    + get_samples(n)
    + add_input(input)
    + add_output(output)
    - note_on_listener(pitch, amplitude)
    - note_off_listener(pitch)
  }
```

```mermaid
---
title: Output
---
classDiagram
  class AudioOutput {
    + new(device, sample_rate)
    + add_input(input)
    + add_effect(effect)
  }
```
