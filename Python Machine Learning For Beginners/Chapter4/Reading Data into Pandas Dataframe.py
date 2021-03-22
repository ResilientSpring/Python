import pandas as pd

url = "https://raw.githubusercontent.com/osias1997/python_pandas_data_analyse/master/data/titanic.csv";
titanic_data = pd.read_csv(url);
data_frame = titanic_data.head();
print(data_frame);