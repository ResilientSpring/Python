import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rc('font', family="MS Gothic")


def gradient_image(ax, extent, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Draw a gradient image based on a colormap.

    Parameters
    ----------
    ax : Axes
        The axes to draw on.
    extent
        The extent of the image as (xmin, xmax, ymin, ymax).
        By default, this is in Axes coordinates but may be
        changed using the *transform* keyword argument.
    direction : float
        The direction of the gradient. This is a number in
        range 0 (=vertical) to 1 (=horizontal).
    cmap_range : float, float
        The fraction (cmin, cmax) of the colormap that should be
        used for the gradient, where the complete colormap is (0, 1).
    **kwargs
        Other parameters are passed on to `.Axes.imshow()`.
        In particular useful is *cmap*.
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, extent=extent, interpolation='bicubic',
                   vmin=0, vmax=1, **kwargs)
    return im


def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top), cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))


# arange automatically balloons into a list with 29 elements from 1 to 28. [2]
year_num = np.arange(0, 29, 1)
print(year_num)

year_num2 = range(0, 29, 1)
print(year_num2)

number_of_births = [176040, 87874, 74498, 38787, 39508]

# xmin, xmax = xlim = 0, 10
ymin, ymax = ylim = 150000, 330000

fig, ax = plt.subplots()
ax.set(ylim=ylim, autoscale_on=False)

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes, cmap=plt.cm.RdYlGn,
               cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
ax.set_aspect('auto')


plt.show()

# References:
# 1. https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html
# 2. https://numpy.org/doc/stable/reference/generated/numpy.arange.html
