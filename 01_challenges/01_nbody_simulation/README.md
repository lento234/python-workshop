# N-body simulation

## Description

This is a classic gravitational n-body simulation problem. The goal is to simulate the graviational interaction of a system of particles $p_i\in P$ where $i=[0,1,...,N]$.

A particle $p_i$ is defined by the following properties:

- mass $m_i$
- position $\mathbf{x}_i = (x_i, y_i, z_i)^\top$
- velocity $\mathbf{u}_i = (u_i, v_i, z_i)^\top$

The particle interact with each other by [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation). Each particle $p_j$ induce a for on particle $p_i$:

$$
F_i = G \sum_i \frac{m_i m_j}{r^2}
$$


## References

**Warning: possible spoiler**

- [https://medium.com/swlh/create-your-own-n-body-simulation-with-python-f417234885e9]
