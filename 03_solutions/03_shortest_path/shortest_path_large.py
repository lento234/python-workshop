import heapq
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

np.random.seed(234)
plt.ion()

from shortest_path import find_shortest_path

def plot(ax, dist, shortest_path, i):
    ax.cla()
    ax.imshow(dist[i], vmin = dist[-1].min(), vmax=dist[-1].max())
    ax.plot(shortest_path[i][0], shortest_path[i][1], c='tab:red')
    ax.axis('off')
    plt.pause(0.0001)

def main():
    plot_freq = 100

    # Open file
    with open("map.txt", 'r') as f:
        map = np.array(
            [list(line.strip()) for line in f.readlines()],
            dtype = 'uint8'
        )

    # Find shortest path
    dist, shortest_path = find_shortest_path(map, start=(0,0))

    # Animate
    fig = plt.figure(figsize=(6,6), dpi=80)
    ax = fig.gca()
    for i in tqdm(range(0, len(dist), plot_freq)):
        plot(ax, dist, shortest_path, i)
    plot(ax, dist, shortest_path, -1)
    plt.waitforbuttonpress()

if __name__ == "__main__":
    main()