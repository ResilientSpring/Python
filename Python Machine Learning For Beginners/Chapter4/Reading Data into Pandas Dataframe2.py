import pandas as pd

url = "https://raw.githubusercontent.com/harikrishna9/titanic_data.csv/main/titanic_data.csv";
titanic_data = pd.read_csv(url);
snoop = titanic_data.head();
print(snoop);