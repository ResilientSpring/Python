import pandas as pd

# Need not enclose a dict{} with [] unless you pass more than one dict{} to the data=
df = pd.DataFrame(data=
    {"User interest": ["Tech", "Fashion", "Fashion", "Sports", "Tech", "Tech", "Sports"],
    "User occupation": ["Professional", "Student", "Professional", "Student", "Student", "Retired", "Professional"],
    "Click": [1, 0, 0, 0, 1, 0, 1]} )

"""
df1 = pd.DataFrame(columns=["User occupation", "Click"],
                   data=[["Professional", 1],
                         ["Student", 0],
                         ["Professional", 0],
                         ["Student", 0],
                         ["Student", 1],
                         ["Retired", 0],
                         ["Professional", 1]
                         ])

df1["User interest"] = ["Tech", "Fashion", "Fashion", "Sports", "Tech", "Tech", "Sports"]

df1.reindex(columns=["User interest", "User occupation", "Click"])
"""

print(df)
