import numpy as np
import matplotlib.pyplot as plt
plt.ion()

np.random.seed(234)

# Constants
G = 1.0
dt = 0.01
epsilon = 0.1
steps = 1000

# Particle
N = 100
m = 20 * np.ones(N)

# Generate particles
x = np.random.randn(N)
y = np.random.randn(N)

# Show
fig, ax = plt.subplots()
ax.plot(x,y, '.')
ax.axis('scaled')
plt.pause(5)
