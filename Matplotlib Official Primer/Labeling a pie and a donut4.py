import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

#  We can use the legend's bbox_to_anchor argument
#  to position the legend outside of the pie.
#  Here we use the axes coordinates (1, 0, 0.5, 1) together with the location "center left";
#  i.e. the left central point of the legend will be at the left central point of the bounding box,
#  spanning from (1, 0) to (1.5, 1) in axes coordinates.
ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(0.1, 0.5, 1., .102))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()

# References:
# 1. https://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
# 2. https://stackoverflow.com/questions/39803385/what-does-a-4-element-tuple-argument-for-bbox-to-anchor-mean-in-matplotlib/39806180#39806180
