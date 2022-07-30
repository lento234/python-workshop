import numpy as np
from tqdm import tqdm
from numba import jit, prange
import matplotlib.pyplot as plt
plt.ion()

np.random.seed(17)

@jit(nopython=True, parallel=True, boundscheck=False)
def update_acceleration_numba(x, a, m, G, epsilon):
    N = x.shape[1]
    for i in prange(N):
        a[:, i] = 0
        for j in range(N):
            r = x[:, j] - x[:, i]
            inv_rnorm3 = (r[0]**2 + r[1]**2 + r[2]**2 + epsilon**2)**(-1.5)
            a[:, i] += G * (r * inv_rnorm3) * m[j]


class Nbody(object):
    def __init__(self, N=100, d=3, m=20.0, G=1.0, dt=0.01, epsilon=0.1, method='numpy'):
        self.N = N # Number of particles
        self.d = d # Number of dimensions
        self.G = G # Gravitational acceleration constant
        self.dt = dt # time step
        self.m = m # mass
        self.method = method
        self.epsilon = epsilon
        self.t = [0]
        self.KE = []

        self._initialize_particles()
        self._update_acceleration()
        self._update_energy()

    def _initialize_particles(self):
        self.m = self.m * np.ones(self.N)**2 / self.N
        self.x = np.random.randn(self.d, self.N)
        self.u = np.random.randn(self.d, self.N)
        self.u -= np.mean(self.m * self.u, axis=1, keepdims=True) / np.mean(self.m)
        self.a = np.zeros((self.d, self.N))

    def _update_acceleration(self):
        if self.method == 'numpy':
            self.__update_acceleration_numpy()
        else:
            update_acceleration_numba(self.x, self.a, self.m, self.G, self.epsilon)

    def __update_acceleration_numpy(self):
        r = self.x[:, np.newaxis, :] - self.x[:, :, np.newaxis]
        inv_rnorm3 = (r[0]**2 + r[1]**2 + r[2]**2 + self.epsilon**2)**(-1.5)
        self.a[:] = self.G * (r * inv_rnorm3) @ self.m

    def _update_energy(self):
        self.KE.append(0.5 * np.sum(self.m * self.u**2))


    def update(self):
        # 1. Half velocity update
        self.u += self.a * self.dt / 2.0
        # 2. Full Position update
        self.x += self.u * self.dt
        # 3. Update acceleration
        self._update_acceleration()
        # 4. Half velocity update
        self.u += self.a * self.dt / 2.0
        # 5. Update time
        self.t.append(self.t[-1]+self.dt)

        # Update energy
        self._update_energy()

# Show
fig = plt.figure(figsize=(5,8), dpi=80)
gs = plt.GridSpec(3, 1, figure=fig, wspace=0, hspace=0.3)
axes = [
    fig.add_subplot(gs[:2, :]),
    fig.add_subplot(gs[2, :])
]

def plot(axes, t, x, x_hist, KE):
    ax = axes[0]
    ax.cla()
    ax.scatter(x[0], x[1], c='k', s=5)
    ax.scatter(x_hist[:,0], x_hist[:,1], c='b', s=1, alpha=0.1)
    ax.axis([-5, 5, -5, 5])
    ax.set(xlabel='x', ylabel='y')
    ax.set_aspect('equal')

    ax = axes[1]
    ax.cla()
    ax.plot(t, KE, 'k', label='KE')
    ax.set(xlabel='t', ylabel='Energy')
    ax.legend(loc=1)
    # ax.set_aspect(0.0007)
    plt.pause(0.001)

# nbody = Nbody(N = 3)
N_hist = 50
Tend = 100

nbody = Nbody(
    N=100,
    method='numpy'
)

N_steps = int(Tend/nbody.dt)
x_hist = np.tile(nbody.x, (N_hist, 1, 1))

for i in tqdm(range(N_steps)):
    # Plot
    if i % 10 == 0:
        plot(axes, nbody.t, nbody.x, x_hist, nbody.KE)

    # Update
    nbody.update()

    x_hist[i % N_hist] = nbody.x
