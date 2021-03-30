# Seeds can be passed to any of the BitGenerators.
from numpy.random import Generator, PCG64
rg = Generator(PCG64(12345));
vals = rg.standard_normal(10);
print(vals);

# https://numpy.org/doc/stable/reference/random/index.html#quick-start