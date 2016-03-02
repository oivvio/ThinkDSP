import thinkdsp

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)

wave = cos_sig.make_wave(duration=1, start=0, framerate=11025)

wave.plot()
