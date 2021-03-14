# Script28 on page 87 of the textbook.

import pandas as pd
import matplotlib.pyplot as plt

sustained_progress_data = pd.read_csv(r"C:\Users\ted10\OneDrive\IdeaProjects\Python"
                                      r"\Python Machine Learning For Beginners\Chapter5"
                                      r"\2020 Higher Education SPROUT Project.csv"
                                      , encoding="GB18030");

print(sustained_progress_data.to_string());