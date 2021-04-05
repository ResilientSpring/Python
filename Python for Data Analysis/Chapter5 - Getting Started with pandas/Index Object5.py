import pandas as pd

dup_labels = pd.Index(data=["foo", "foo", "bar", "bar"]);
print(dup_labels);