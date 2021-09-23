import matplotlib.pyplot as plt

labels = ['SciFi', 'Drama', 'Thriller', 'Comedy', 'Action', 'Romance']
sizes = [5, 15, 10, 20, 40, 10]  # Add upto 100%

# Show one slice slightly outside the circle.
explode = (0, 0, 0, 0, 0.1, 0)  # only "explode" the 5th slice (i.e. 'Action')

plt.pie(x=sizes, explode=explode, labels=labels, autopct='%1.1%f%%', shadow=True, startangle=90)

# The equal aspect ratio ensures that pie is drawn as a circle. The default is an ellipse.
plt.axis('equal')

plt.show()
