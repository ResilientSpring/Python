import thinkdsp
import matplotlib.pyplot as plt

cos_signal = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sigal = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

mix = sin_sigal + cos_signal

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)

wave.plot()

plt.show()
