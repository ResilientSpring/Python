import pandas as pd

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