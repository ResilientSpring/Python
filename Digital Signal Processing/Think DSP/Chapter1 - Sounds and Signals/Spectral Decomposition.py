import thinkdsp

cos_signal = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sigal = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

mix = sin_sigal + cos_signal
