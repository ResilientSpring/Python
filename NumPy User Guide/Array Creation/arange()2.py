# Numpy.arange([start, ]stop, [step, ], dtype=None, *, like=None)
#     Parameters
#           start : integer or real, optional
#               Start of interval.
#               The interval includes this value. The default start value is 0.
#
#           stop : integer or real
#                End of interval. The interval does not include this value,
#                except in some cases where step is not an integer and floating point
#                round-off affects the length of out.
#
#           step : integer or real, optional
#                Spacing between values. For any output out,
#                this is the distance between two adjacent values, out[i+1] - out[i].
#                The default step size is 1.
#                If step is specified as a position argument, start must also be given.
# Reference:
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html