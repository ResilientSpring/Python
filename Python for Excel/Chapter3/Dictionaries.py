exchange_rates = {"EURUSD": 1.1152, "GBPUSD": 1.2454, "AUDUSD": 0.6161};
print(exchange_rates["EURUSD"]);
# print(exchange_rates{"EURUSD"});

# Change an existing value.
exchange_rates["EURUSD"] = 1.2;

print(exchange_rates);

# Add a new key/value pair.
exchange_rates["CADUSD"] = 0.714;

print(exchange_rates);

# To merge two or more dictionaries is by using two leading asterisks,
# which unpacks them into a new dictionary.
print( {** exchange_rates, ** {"SGDUSD": 0.7004, "GBPUSD": 1.2222}} );
# If the second dictionary contatins keys from the first one, the values from the first
# will be overridden.

# Python 3.9 introduced the pipe character as a dedicated merge operator for dictionaries,
# which allows you to simplify the previous expression to this:
# print(exchange_rates | {"SGDUSD":0.70, "GBPUSD":1.20});