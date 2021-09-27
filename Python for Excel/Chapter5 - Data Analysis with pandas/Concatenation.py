import pandas as pd

more_users = pd.DataFrame(data=[[15, "France", 4.1, "Becky"],
                                [44, "Canada", 6.1, "Leanne"]],
                          columns=['age', 'country', 'score', 'name'],
                          index=[1000, 1011])

print(more_users)

data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]
        ]

df = pd.DataFrame(data=data, columns=["name", "age", "country", "score", "continent"],
                  index=[1001, 1000, 1002, 1003])

glue = pd.concat([df, more_users], axis=0)
print(glue)

glue2 = pd.concat([df, more_users], axis=1)
print(glue2)
