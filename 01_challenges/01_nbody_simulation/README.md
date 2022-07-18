# N-body simulation

## Description

This is a classic gravitational n-body simulation problem. The goal is to simulate the graviational interaction of a system of particles $p_i\in P$ where $i=[1, 2, ...,N]$.

A particle $p_i$ is defined by the following properties:

- mass $m_i$
- position $\mathbf{x}_i = (x_i, y_i, z_i)^\top$
- velocity $\mathbf{u}_i = (u_i, v_i, z_i)^\top$

### Calculating force interactions

The particle interact with each other by [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation). Each particle $p_j$ induce a force on particle $p_i$. The component of force induced by particle $j$ on $i$ is given as:

$$
\mathbf{F}_{ij} = G \sum_i \frac{m_i m_j}{|\mathbf{r}_{ij}|^2}\frac{\mathbf{r}_{ij}}{|\mathbf{r}_{ij}|},
$$

where $G = 6.67\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ is the Gravitational constant and

$$
\mathbf{r}_{ij} = \mathbf{x}_j - \mathbf{x}_i
$$

is the distance vector between the two point masses and $|\mathbf{r}_{ij}|$ is the magnitude (i.e. distance norm).

Using Netwon's second law, we can determine the acceleration experienced by particle $i$ due to all $j$ particles as follows:

$$
\mathbf{a}_i = \frac{1}{m_i} \sum_j \mathbf{F}_{ij} = G \sum_i m_j\frac{\mathbf{r}_{ij}}{|\mathbf{r}_{ij}|^3}.
$$

**Note**: For stability reason, use a damping factor for $|\mathbf{r}_{ij}|$ to ensure denominator is non-zero, i.e., $|\mathbf{r}_{ij}| = \sqrt{(x_j-x_i)^2 + (y_j-y_i)^2 + \epsilon^2}$ with $\epsilon=10^{-1}$.

### Time integration

At each timestep $t_n$, the positions and the velocities of the particle are updated. For n-body simulation, a [Leapfrog integration](https://en.wikipedia.org/wiki/Leapfrog_integration) scheme is used a second-order accurate time integration. The evolution consists of:

1. Half-update of velocity: $\mathbf{u_i} = \mathbf{u_i} + \mathbf{a_i}\frac{\Delta t}{2}$
2. Full-update of position: $\mathbf{x_i} = \mathbf{x_i} + \mathbf{v_i}\Delta t$
3. Finally, half-update of velocity: $\mathbf{u_i} = \mathbf{u_i} + \mathbf{a_i}\frac{\Delta t}{2}$

### Energy

Total energy of the system is given as:

$$
E_{tot} = \frac{1}{2} \sum_i m_i |\mathbf{u}_i|^2 - G\sum_{1 \le i < j \le N} \frac{m_i m_j}{|\mathbf{r}_{ij}|},
$$

where the first-term is the kinetic energy, and second is the potential energy. Note for the potential energy only one interaction if calculated for each point mass pair.


## Challenge

Use `numpy` or `numba` to implement the n-body interaction and time integration. Visualize using `matplotlib`.

1. Simulate a 2D n-body problem from $t=0$ with random **Gaussian** distribution of velocity and position of $N=100$ particles. Assume, $G=1.0$, $dt=0.01$, $\epsilon=0.1$ and $m_i=20$. Simulate for 1000 iteration till $t=10$.
2. Visualize the motion of the particles using matplotlib. Same every 10th frame and convert to an animation using matplotlib.
3. *Optional*: Plot the evolution of kinetic, potential and total energy of the system.
4. *Optional*: Extend the problem to 3D and visualize. Play around with larger number of particles

## References

*Warning: spoiler*

- [https://medium.com/swlh/create-your-own-n-body-simulation-with-python-f417234885e9]
