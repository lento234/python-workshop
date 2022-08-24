import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
plt.ion()

np.random.seed(1234)

grid_size = 64
init_prob = 0.9 # 15 %
steps = 10000
plot_freq = 1
grid = (np.random.rand(grid_size, grid_size) > init_prob).astype('uint8')

stencil = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

def update(grid, stencil, mode='wrap'):
    neigbors = scipy.ndimage.convolve(grid, stencil, mode=mode)
    return np.logical_or(
        np.logical_and(grid, (neigbors == 2) | (neigbors == 3)),
        np.logical_and(1-grid, neigbors == 3)
    ).astype('uint8')


def update_plot(ax, grid, i):
    ax.cla()
    ax.imshow(grid, cmap='gray_r')
    ax.text(0.85, 0.02, f'step {i:04d}', transform=ax.transAxes)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.tight_layout()
    # Wait
    plt.pause(0.0001)

# Setup plot
fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.gca()

for i in range(steps):
    # Update state
    grid = update(grid, stencil)
    # Update plot
    if i % plot_freq == 0:
        update_plot(ax, grid, i)


plt.waitforbuttonpress()
