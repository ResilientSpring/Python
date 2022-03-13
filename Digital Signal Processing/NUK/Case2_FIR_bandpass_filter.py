from math import pi, cos
import numpy as np
import matplotlib.pyplot as plt

N = 40;
ws1 = 0.3*pi;
wp1 = 0.4*pi;
wp2 = 0.65*pi;
ws2 = 0.75 * pi;
Ns = 200;

NH = N / 2;
deltaw = pi/ Ns;
Ns_p = round((wp2 - wp1)/deltaw);
Ns_s1 = round(ws1/deltaw);
Ns_s2 = round((pi - ws2) / deltaw);
NV = []

for i in range(NH):
    NV.append(i)


NV = np.array(NV)
NV = NV.transpose()

P = np.zeros(NH, 1);
Qp = np.zeros(NH, NH);

for iw in range(Ns_p):
    w = wp1 + iw*deltaw;
    P = P - 2*cos(w*(NV-0.5));
    Qp = Qp + cos(w * (NV-0.5)) * np.array((cos(w * (NV-0.5)))).transpose()


P = (wp2 - wp1) * P / (Ns_p + 1);
Qp = (wp2 - wp1) * Qp / (Ns_p + 1);

Qs = np.zeros(NH, NH)

for iw in range(Ns_s1):
    w = iw*deltaw;
    Qs1 = Qs1 + cos(w*(NV-0.5)) * np.array((cos(w*(NV-0.5)))).transpose()


Qs1 = ws1 * Qs1 / (Ns_s1 + 1);

Qs2 = np.zeros(NH, NH);

for iw in range(Ns_s2):
    w = ws2 + iw*deltaw;
    Qs2 = Qs2 + cos(w*(NV-0.5)) * np.array((cos(w*(NV-0.5)))).transpose()


Qs2 = (pi - ws2) * Qs2 / (Ns_s2 + 1);

Q = Qp + Qs1 + Qs2;
A = -0.5 * np.invert(Q) * P

h = np.zeros(N, 1)
h[1:NH] = 0.5 * np.flipud(A)
h[NH+1:N] = 0.5 * A


