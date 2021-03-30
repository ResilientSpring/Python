# The preferred best practice for getting reproducible pseudorandom numbers is
# to instantiate a generator object with a seed and pass it around.
# The implicit global RandomState behind the numpy.random.* convenience functions
# can cause problems, especially when threads or other forms of concurrency
# are involved. Global state is always problematic.
# We categorically recommend avoiding using the convenience functions when
# reproducibility is involved.

# https://numpy.org/neps/nep-0019-rng-policy.html