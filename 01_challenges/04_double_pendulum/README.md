# Double pendulum problem

## Description

![Double pendulum](https://upload.wikimedia.org/wikipedia/commons/7/78/Double-Pendulum.svg)

A [double pendulum](https://en.wikipedia.org/wiki/Double_pendulum) is a classic dynamic problem. The problem is sensitive to initial conditions resulting in a chaotic motion. Th positions of the mass is given as:

* $\mathbf{x}_1 = (x_1, y_1) = L_1(\sin \theta_1, -\cos \theta_1)$
* $\mathbf{x}_2 = (y_2, y_2) = (L_1 \sin \theta_1 + L_2 \sin \theta_2, -L_1 \cos \theta_1 - L_2 \cos \theta_2)$

### Equation of motion

The equation of motion for the double pendulum by looking at the Lagrangian of system. The Lagrangian is $L = T - V$. The kinetic energy ($T$) of the system is:

$$
T = T_1 + T_2 = \frac{1}{2} m_1 (\ddot{x}_1^2 + \ddot{y}_1^2) + \frac{1}{2} m_2 (\ddot{x}_2^2 + \ddot{y}_2^2)
$$

The total potential energy $V$ of the system is given as:

$$
V = V_1 + V_2 = m_1 g y_1 + m_2 g y_2
$$

and so the Lagrangian of the system is given as:

$$
L = (T_1 + T_2) - (V_1 + V_2)
$$

The equation of motion is derived by balancing the linear and angular momentum of the system, by using the Lagrange's equation:

$$
\frac{\partial L}{\partial \theta_1} - \frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_1} = 0 \\
\frac{\partial L}{\partial \theta_2} - \frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_2} = 0
$$

and so we a have a second-order PDE.


## Challenge

Solve the double pendulum problem using an **ODE** solver. You can solve using scipy's [`solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp) function. Use the following initial conditions: $g=9.81$, $m_1=2$, $m_2=1$, $L_1=2$, $L_2=1$, $\theta_1=1$, $\dot{\theta_1}=-3$, $\theta_2=-1$, $\dot{\theta_2}=5$, $t=0$, $dt=0.04$, $t_N=40$.

1. Solve the double-pendulum problem using `scipy`, `numpy`, and if needed `sympy` (for symbolic computations).
2. Visualize the motion of the pendulum using `matplotlib`.
3. *Optional*: Plot the evolution of the Lagrangian of the system.

## References

*Warning: spoilers*

- https://scipython.com/blog/the-double-pendulum/
- https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid23.ipynb
