import pandas as pd

df = pd.DataFrame(data={"score": ["low", "high", "medium", "medium", "low"]});
print(df);

mapping = {"low": 1, "medium": 2, "high": 3};
print(mapping);

df["score"] = df["score"].replace(mapping);

print(df);