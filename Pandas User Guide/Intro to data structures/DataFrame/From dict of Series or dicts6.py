import pandas as pd

s1 = pd.Series(data=[1.0, 2.0, 3.0], index=['a', 'b', 'c'], dtype=float, name="Series 1");
print(s1);

s2 = pd.Series(data=[1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'], dtype=float,
               name="Series 2");
print(s2);

dictionary = {"one": s1, "two": s2};

print(dictionary);

dataFrame = pd.DataFrame(data=dictionary, index=['a', 'b', 'c', 'd'],
                         columns=["lifeblood", "livelihood"], );
print(dataFrame);

print(dataFrame.index, dataFrame.columns, dataFrame.info());