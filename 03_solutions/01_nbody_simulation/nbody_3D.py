import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

# Nbody solver
from nbody import Nbody

plt.ion() # Interactive on
np.random.seed(234) # RNG seed


def main():
    # Initialize nbody system
    nbody = Nbody(
        N = 4, m = 20, dt = 0.01, G = 2.0,
        epsilon = 0.1, d = 3,
    )

    # Simulation configurations
    Tend = 100
    N_hist = 1000
    plot_freq = 10

    N_steps = int(Tend/nbody.dt)
    x_hist = np.tile(nbody.x, (N_hist, 1, 1))

    # Setup plot
    fig = plt.figure(figsize=(6,6), dpi=80)
    ax = fig.add_subplot(projection='3d')

    # Evolve
    for i in tqdm(range(N_steps)):
        # Update
        nbody.step()

        # Store past positions
        x_hist[i % N_hist] = nbody.x

        # Plot
        if not plt.fignum_exists(fig.number): break
        if i % plot_freq == 0:
            ax.cla()
            ax.scatter(nbody.x[0], nbody.x[1], nbody.x[2], c='tab:blue', s=50)
            ax.scatter(x_hist[:,0], x_hist[:,1], x_hist[:, 2], c='tab:red', s=1, alpha=0.1)
            ax.set(xlabel='x', ylabel='y', zlabel='z',
                   xlim=(-5,5), ylim=(-5, 5), zlim=(-5, 5))
            ax.view_init(elev=20.0, azim=i/10)
            plt.pause(0.001)


if __name__ == "__main__":
    main()
