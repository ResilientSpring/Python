import pandas as pd

df = pd.DataFrame(data=[["green", 'M', 10.1, "class2"],
                        ["red", 'L', 13.5, "class1"],
                        ["blue", "XL", 15.3, "class2"]
                        ])

df.columns = ["color", "size", "price", "class_label"]

print(df)