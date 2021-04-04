# Input[38] on Page 174

import pandas as pd

sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000};
print(sdata);

obj3 = pd.Series(sdata);
print(obj3);

obj4 = pd.Series(data=sdata, index=["California", "Ohio", "Oregon", "Texas"]);
print(obj4);

obj4.name = "population";
obj4.index.name = "State";
print(obj4);