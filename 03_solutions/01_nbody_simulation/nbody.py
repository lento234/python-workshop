import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

plt.ion() # Interactive on
np.random.seed(234) # RNG seed

class Nbody:
    def __init__(self, N, m, dt, G=1.0, epsilon=0.1, d=2):
        """Nbody particle system

        Args:
            N (int): Number of particles.
            m (float): Total mass of particle system.
            dt (float): Time step size.
            G (float, optional): Gravitational constant. Defaults to 1.0.
            epsilon (float, optional): Resiprocal distance damping factor. Defaults to 0.1.
            d (int, optional): Number of dimensions. Defaults to 2.
        """

        # Settings
        self.N = N # Number of particles
        self.d = d # Number of dimensions
        self.G = G # Gravitational acceleration constant
        self.dt = dt # time step
        self.epsilon = epsilon

        # Initial conditions
        self.t = [0]
        self.E = {'K': [], 'P': [], 'T': []}

        self.m = m * np.ones(self.N) / self.N
        self.x = np.random.randn(self.d, self.N)
        self.u = np.random.randn(self.d, self.N)
        self.u -= np.mean(self.m * self.u, axis=1, keepdims=True) / np.mean(self.m)
        self.a = np.zeros((self.d, self.N))

        # Update acceleration and energy
        self.__update_acceleration()
        self.__update_energy()

    def __update_acceleration(self):
        """Update acceleration.
        """
        r = self.x[:, np.newaxis, :] - self.x[:, :, np.newaxis]
        inv_rnorm3 = 1/(np.linalg.norm(r, axis=0) + self.epsilon)**3
        self.a[:] = self.G * (r * inv_rnorm3) @ self.m

    def __update_energy(self):
        """Update energy.
        """
        # Kinetic energy
        self.E['K'].append(0.5 * np.sum(self.m * self.u**2))

        # Potential energy
        inv_rnorm = 1/(np.linalg.norm(self.x[:, np.newaxis, :] - self.x[:, :, np.newaxis], axis=0) + self.epsilon)
        self.E['P'].append(np.sum(- self.G * (self.m * np.tril(inv_rnorm)) @ self.m))

        # Total energy
        self.E['T'].append(self.E['K'][-1] + self.E['P'][-1])



    def step(self):
        """Time stepping method.
        """
        # 1. Half velocity update
        self.u += self.a * self.dt / 2.0
        # 2. Full Position update
        self.x += self.u * self.dt
        # 3. Update acceleration
        self.__update_acceleration()
        # 4. Half velocity update
        self.u += self.a * self.dt / 2.0
        # 5. Update energy
        self.__update_energy()
        # 6. Update time
        self.t.append(self.t[-1]+self.dt)


def update_plot(axes, **kwargs):
    # Get variables
    t = kwargs['t']
    x = kwargs['x']
    x_hist = kwargs['x_hist']
    E = kwargs['E']

    ax = axes[0]
    ax.cla()
    ax.scatter(x[0], x[1], c='tab:blue', s=15)
    ax.scatter(x_hist[:,0], x_hist[:,1], c='tab:red', s=1, alpha=0.1)
    ax.axis([-5, 5, -5, 5])
    ax.set(xlabel='x', ylabel='y')
    ax.set_aspect('equal')

    ax = axes[1]
    ax.cla()
    for key in E.keys():
        ax.plot(t, E[key], label=key)
    ax.set(xlabel='t', ylabel='Energy')
    ax.legend(loc=1)
    plt.pause(0.001)

def main():
    # Initialize nbody system
    nbody = Nbody(
        N = 100,
        m = 20,
        dt = 0.01,
        G = 2.0,
        epsilon = 0.1,
    )

    # Simulation configurations
    Tend = 100
    N_hist = 50
    plot_freq = 10

    N_steps = int(Tend/nbody.dt)
    x_hist = np.tile(nbody.x, (N_hist, 1, 1))

    # Setup plot
    fig = plt.figure(figsize=(6,8), dpi=80)
    gs = plt.GridSpec(3, 1, figure=fig, wspace=0, hspace=0.3)
    axes = [
        fig.add_subplot(gs[:2, :]),
        fig.add_subplot(gs[2, :])
    ]

    # Evolve
    for i in tqdm(range(N_steps)):
        # Update
        nbody.step()

        # Store past positions
        x_hist[i % N_hist] = nbody.x

        # Plot
        if i % plot_freq == 0:
            update_plot(
                axes, t=nbody.t, x=nbody.x, x_hist=x_hist, E=nbody.E,
            )
        elif not plt.fignum_exists(fig.number):
            break


if __name__ == "__main__":
    main()
