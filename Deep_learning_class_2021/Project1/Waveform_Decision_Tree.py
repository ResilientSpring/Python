import pandas as pd

url = "https://raw.githubusercontent.com/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/waveform.data"

waveform_data = pd.read_csv(filepath_or_buffer=url, header=None)
print(waveform_data)



