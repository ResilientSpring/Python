import Time_Series_Generator

number_of_steps = 50

series = Time_Series_Generator.generate_time_series(batch_size=10000,
                                                    number_of_steps=number_of_steps + 10)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -10, 0]

print(X_train)
print('='*30)
print(y_train)
