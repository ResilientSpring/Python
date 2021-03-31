from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence

rs = RandomState(MT19937(SeedSequence(123456789)));
print(rs);

# Later, you want to restart the stream
rs = RandomState(MT19937(SeedSequence(987654321)));
print(rs);

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html