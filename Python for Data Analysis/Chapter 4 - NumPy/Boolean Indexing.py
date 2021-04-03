import numpy as np

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"]);
print(names);
print(names == "Bob");
print(names != "Bob");
print(~(names == "Bob"));  # ~ means !

data = np.random.randn(7, 4);
print(data);