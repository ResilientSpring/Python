def print_values(**kwargs):
    for key,value in kwargs.items():
        print("The value of {} is {}".format(key, value));

print_values(my_name="Sammy", your_name="Casey");