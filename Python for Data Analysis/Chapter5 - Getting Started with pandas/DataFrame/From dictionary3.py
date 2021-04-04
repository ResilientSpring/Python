import pandas as pd

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};

frame = pd.DataFrame(data=data, columns=["year", "state", "pop", "debt"],
                     index=["one", "two", "three", "four", "five", "six"]);
print(frame);

# A column in DataFrame can be retrieved as a Series either by dict-like notation
print(frame["state"]);

# or by attribute:
print(frame.year);

# Reference:
# The Input[51] on Textbook page on 176.