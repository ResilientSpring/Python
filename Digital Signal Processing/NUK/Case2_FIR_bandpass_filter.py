from math import pi, cos
import numpy as np

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

