import pandas as pd
import numpy as np

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};

frame = pd.DataFrame(data=data, columns=["year", "state", "pop", "debt"],
                     index=["one", "two", "three", "four", "five", "six"]);
print(frame);

print(frame.columns);
print(frame["year"]);

# assign new value to the column of debt.
frame["debt"] = 16.5;

print(frame);

frame["debt"] = np.arange(6.);
print(frame);

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