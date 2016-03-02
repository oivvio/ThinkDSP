import thinkdsp
import thinkplot
import random
from IPython.display import display

signals = []
start = 100
stop = 2000
n = 10
for i in range(n):
    freq = random.randint(100, 1000)
    signals.append(thinkdsp.SinSignal(freq=freq, amp=1.0, offset=0))
sig = sum(signals)

print(sig.period, 1/sig.period)

wave = sig.make_wave(duration=0.1/sig.period, start=0, framerate=22050)

audio = wave.make_audio()
display(audio)

# spectrum = wave.make_spectrum()
# spectrum.plot(high=1100)
thinkplot.show()
