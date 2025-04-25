import matplotlib.pyplot as plt
import numpy as np

def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """Draw a gradient image based on a colormap."""
    v = np.array([np.cos(direction * np.pi / 2), np.sin(direction * np.pi / 2)])
    X = np.array([[0, 0], [v[0], v[1]]])
    Y = np.array([[0, 0], [-v[1], v[0]]])
    extent = (np.min(X), np.max(X), np.min(Y), np.max(Y))

    Z = np.empty((100, 100))
    for i in range(100):
        for j in range(100):
            Z[i, j] = (i/99)*v[0] + (j/99)*v[1]

    img = ax.imshow(Z, extent=extent, aspect='auto', cmap=plt.get_cmap('viridis'), vmin=cmap_range[0], vmax=cmap_range[1], origin='lower', **kwargs)
    return img



# Sample data
x = np.arange(5)
y = np.random.rand(5)

fig, ax = plt.subplots()

# Create the gradient image
gradient = gradient_image(ax, direction=1)
gradient.set_clip_path(ax.patch)  # Clip the gradient to the axes

# Create bars and set facecolor to "none" to allow gradient visibility
bars = ax.bar(x, y)
for bar in bars:
    bar.set_facecolor("none")
    xpos = bar.get_x()
    width = bar.get_width()
    height = bar.get_height()

    # Add a clipped image for each bar
    ax.imshow(gradient.get_array(), extent=[xpos, xpos+width, 0, height], aspect='auto', cmap=plt.get_cmap('viridis'), vmin=0, vmax=1, clip_on=True)

ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Gradient Colors')

plt.show()

# Source: https://www.google.com/search?q=matplotlib+bar+color+gradient