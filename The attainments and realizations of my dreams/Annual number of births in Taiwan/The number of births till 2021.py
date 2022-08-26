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

year_num = list(year_num)

year_num2 = range(0, 30, 1)
print(year_num2)

number_of_births = [322938, 329581, 325545, 326002, 271450, 283661, 305312, 260354, 247530, 227070,
                    216419, 205854, 204459, 204414, 198733, 191310, 166886, 196627, 229481, 199113,
                    210383, 213598, 208440, 193844, 181601, 177767, 165249, 153820,
                    (13137, 9617, 12788, 11222, 9442, 10943, 10950)]

label_year = np.arange(1994, 2023, 1)
print(label_year)

label_year_text = ["1994", "'95", "'96", "'97", "'98", "'99", "2000", "'01", "'02", "'03", "'04", "'05",
                   "'06", "'07", "'08", "'09", "'10", "'11", "'12", "'13", "'14", "'15", "'16", "'17",
                   "'18", "'19", "'20", "'21", "'22"]

# xmin, xmax = xlim = 0, 10
ymin, ymax = ylim = 150000, 330000

fig, axe = plt.subplots(nrows=1, ncols=1, figsize=(8, 7))
axe.set(ylim=ylim, autoscale_on=False)

# background image
gradient_image(axe, direction=1, extent=(0, 1, 0, 1), transform=axe.transAxes, cmap=plt.cm.RdYlGn,
               cmap_range=(0.2, 0.8), alpha=0.5)


axe.set_aspect('auto')
axe.set_xlabel("Year")
axe.set_ylabel("The number of births")
axe.set_title(label="1994-2022/07 台灣年度出生人數\n Annual number of births in Taiwan", fontsize=20)

plt.xticks(year_num, labels=label_year_text, rotation=7, fontsize=12)
plt.tick_params(axis='y', labelsize=12)

gradient_bar(ax=axe, x=label_year, y=number_of_births, width=0.7)

plt.show()

# References:
# 1. https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html
# 2. https://numpy.org/doc/stable/reference/generated/numpy.arange.html

# Data: https://statis.moi.gov.tw/micst/stmain.jsp?sys=220&ym=8300&ymt=11000&kind=21&type=1&funid=c0120101&cycle=4&outmode=0&compmode=0&outkind=1&fld0=1&cod00=1&rdm=fu0Necq9
