from thinkdsp import CosSignal, SinSignal, decorate
import matplotlib.pyplot as plt

cosine_signal = CosSignal(freq=440, amp=1.0, offset=0)

sine_signal = SinSignal(freq=880, amp=0.5, offset=0)

cosine_signal.plot()
decorate(xlabel='Time (s)')

# figure, (axes1, axes2) = plt.subplots(nrows=2)

# axes1.plot(cosine_signal)
# axes1.set_xlabel('Time (s)')

plt.show()
