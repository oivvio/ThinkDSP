import thinkdsp
import thinkplot

afile = "/tmp/temp.wav"
# sig1 = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
# sig2 = thinkdsp.CosSignal(freq=100, amp=1.0, offset=0)


# sig = sig1 + sig2
# wave = sig.make_wave(duration=1, start=0, framerate=11025)

sig = thinkdsp.TriangleSignal(freq=1100, amp=1, offset=0)
#sig = thinkdsp.SinSignal(freq=1100, amp=1, offset=0)

wave = sig.make_wave(duration=1, framerate=10000)
#wave.plot()
wave.play(afile)
spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.show()
