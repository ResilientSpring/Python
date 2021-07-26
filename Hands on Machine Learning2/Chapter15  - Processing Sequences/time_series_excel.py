import Time_Series_Generator as t
import pandas as pd

series = t.generate_time_series(batch_size=100, number_of_steps=51)

print(series.shape)
