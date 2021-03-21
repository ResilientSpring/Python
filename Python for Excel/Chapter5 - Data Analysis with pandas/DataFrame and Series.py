import pandas as pd

sheet = pd.read_excel(r"C:\Users\ted10\OneDrive\IdeaProjects\Python\Python for Excel\Companion "
                      r"repository\xl\course_participants.xlsx");
print(sheet.to_string());