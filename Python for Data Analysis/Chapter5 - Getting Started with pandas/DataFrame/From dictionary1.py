import pandas as pd

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};

frame = pd.DataFrame(data=data);
print(frame);

frame2 = pd.DataFrame(data=data, columns=["year", "state", "pop"]);
print(frame2);

# If you pass a column that is not contained in the dict,
# it will appear with missing values in the result:
frame3 = pd.DataFrame(data=data, columns=["year", "state", "pop", "debt"],
                      index=["one", "two", "three", "four", "five", "six"]);
print(frame3);
print(frame3.columns, "\n", frame3.index);