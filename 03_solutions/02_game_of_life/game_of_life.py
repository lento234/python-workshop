import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

plt.ion() # Interactive on
np.random.seed(234) # RNG seed

def update(grid, stencil, mode='wrap'):
    """State update function using `scipy.ndimage.convolve` method.

    Args:
        grid (ndarray): Population state grid
        stencil (ndarray): Neighborhood stencil to apply the rule.
        mode (str, optional): How to treat boundary. Defaults to 'wrap'.

    Returns:
        ndarray: Update populate state
    """
    neigbors = scipy.ndimage.convolve(grid, stencil, mode=mode)
    return np.logical_or(
        np.logical_and(grid, (neigbors == 2) | (neigbors == 3)),
        np.logical_and(1-grid, neigbors == 3)
    ).astype('uint8')


def main():
    # Initial conditions
    grid_size = 64
    init_prob = 0.85 # 80 %

    # Runtime options
    steps = 3000
    plot_freq = 1

    # Initilize field
    grid = (np.random.rand(grid_size, grid_size) > init_prob).astype('uint8')

    # Neighborhood stencil
    stencil = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    # Setup plot
    fig = plt.figure(figsize=(6,6), dpi=80)
    ax = plt.gca()

    for i in range(steps):
        # Update state
        grid = update(grid, stencil)
        if not plt.fignum_exists(fig.number):
            # Stop if figure closed
            break
        elif i % plot_freq == 0:
            # Update plot
            ax.cla()
            ax.matshow(grid, cmap='gray_r')
            ax.text(0.9175, 0.02, f'{i:04d}',
                    weight='bold',
                    bbox=dict(facecolor='white', alpha=0.8),
                    transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            plt.tight_layout()
            plt.pause(0.01) # wait to draw

if __name__ == "__main__":
    main()
