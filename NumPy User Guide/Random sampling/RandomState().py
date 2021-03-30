# A fixed seed and a fixed series of calls to RandomState methods using
# the same parameters will always produce the same results up to roundoff
# error except when the values were incorrect.

# The purpose of RandomState will be documented as providing certain fixed functionality
# for backwards compatibility and stable numbers for the limited purpose of unit testing,
# and not making whole programs reproducible across numpy versions.

# Further reading:
# Abstract:
# we have obligated the random number distributions to always produce the exact
# same numbers in every version. The objective of our stream-compatibility guarantee
# was to provide exact reproducibility for simulations across numpy versions
# in order to promote reproducible research.

# https://numpy.org/neps/nep-0019-rng-policy.html