import Time_Series_Generator

number_of_steps = 50

series = Time_Series_Generator.generate_time_series(batch_size=10000,
                                                    number_of_steps=number_of_steps + 10)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -10, 0]

print(X_train)
print(X_train.shape)
print('='*30)
print(y_train)
print(y_train.shape)
print('='*30)

print(series[:5, -10])
print('='*30)
print(series[:5, 0])
print('='*30)
print(series[:5, -10, 0])
