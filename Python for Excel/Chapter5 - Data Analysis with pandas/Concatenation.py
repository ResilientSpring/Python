import pandas as pd

more_users = pd.DataFrame(data=[[15, "France", 4.1, "Becky"],
                                [44, "Canada", 6.1, "Leanne"]],
                          columns=['age', 'country', 'score', 'name'],
                          index=[1000, 1011])

print(more_users)
