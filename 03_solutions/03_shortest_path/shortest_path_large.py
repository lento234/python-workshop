import heapq

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

np.random.seed(234)
plt.ion()

from shortest_path import find_shortest_path


def plot(ax, map, dist, shortest_path, i):
    ax.cla()
    cur_dist = dist[i].astype("float64")
    cur_dist[cur_dist == np.iinfo(dist[i].dtype).max] = np.nan
    ax.imshow(map)
    ax.imshow(cur_dist, vmin=dist[-1].min(), vmax=dist[-1].max())
    ax.contour(np.isnan(cur_dist), levels=[0.5], colors="w", linewidths=[2])
    ax.plot(shortest_path[i][0], shortest_path[i][1], c="tab:red", lw=2)
    ax.axis("off")
    plt.pause(0.0001)


def main():
    plot_freq = 50

    # Open file
    with open("map.txt", "r") as f:
        map = np.array([list(line.strip()) for line in f.readlines()], dtype="uint8")

    # Find shortest path
    dist, shortest_path = find_shortest_path(map, start=(0, 0))

    # Animate
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.gca()
    for i in tqdm(range(0, len(dist), plot_freq)):
        plot(ax, map, dist, shortest_path, i)
    plot(ax, map, dist, shortest_path, -1)
    plt.waitforbuttonpress()


if __name__ == "__main__":
    main()
