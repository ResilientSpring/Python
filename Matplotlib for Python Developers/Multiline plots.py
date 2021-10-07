import matplotlib.pyplot as plt

date = [11, 12, 13, 14, 15, 16, 17]

temperature0 = [15.3, 15.4, 12.6, 12.7, 13.2, 12.3, 11.4]
temperature1 = [26.1, 26.2, 24.3, 25.1, 26.7, 27.8, 26.9]
temperature2 = [22.3, 20.6, 19.8, 21.6, 21.3, 19.4, 21.4]

# plot the lines for each data series
plt.plot(date, temperature0)
plt.plot(date, temperature1)
plt.plot(date, temperature2)

plt.show()
