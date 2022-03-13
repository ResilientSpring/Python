from math import pi

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

