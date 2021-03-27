import pandas as pd

data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]
        ];

df = pd.DataFrame(data=data, columns=["name", "age", "country", "score", "continent"],
                  index=[1001, 1000, 1002, 1003]);

print(df.info());

print("---------------Separation line------------------");

print(df.info);