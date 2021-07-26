import Time_Series_Generator as t

series = t.generate_time_series(batch_size=1, number_of_steps=2)
print(series)