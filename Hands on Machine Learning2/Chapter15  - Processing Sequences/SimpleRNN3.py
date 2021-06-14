import Time_Series_Generator as time

number_of_steps = 50
series = time.generate_time_series(batch_size=10000, number_of_steps=number_of_steps + 1)

print(series)
print(series.shape)
