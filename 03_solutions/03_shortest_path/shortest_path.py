import heapq
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(234)
plt.ion()

def find_neighbors(p, nrows, ncols):
    row, col = p
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < (nrows - 1):
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < (ncols - 1):
        neighbors.append((row, col + 1))
    return neighbors

def trace_path(prev, start, p):
    p_cur = p
    shortest_path = [p_cur]
    while p_cur != start:
        p_cur = tuple(prev[p_cur[0], p_cur[1]])
        shortest_path.append(p_cur)
    return np.asarray(shortest_path)[::-1].T

def find_shortest_path(map, start=(0, 0), dest=None):
    nrows, ncols = map.shape

    if dest is None:
        dest = (nrows-1, ncols-1)

    # Init Priority queue
    queue = [(0, start)]

    dist = np.full((nrows, ncols), fill_value=-1, dtype=np.uint64)
    dist[start] = 0

    # Initialize predecessor node map
    prev = np.full((nrows, ncols, 2), fill_value=0, dtype="uint64")

    dist_snapshots = [np.copy(dist)]
    shortest_path_snapshots = []

    # Store visited set of nodes
    visited_nodes = set()

    while queue:
        _, p = heapq.heappop(queue)

        if p == dest:
            break

        visited_nodes.add(p)

        # Travel to all neighbors
        for p_nbr in find_neighbors(p, nrows, ncols):
            new_dist = dist[p] + map[p_nbr]

            if new_dist < dist[p_nbr]:
                dist[p_nbr] = new_dist
                heapq.heappush(queue, (new_dist, p_nbr))
                prev[p_nbr] = p

        # Find shortest paths
        dist_snapshots.append(np.copy(dist))
        shortest_path_snapshots.append(trace_path(prev, start, p))

    # Final path
    shortest_path_snapshots.append(trace_path(prev, start, p))

    return dist_snapshots, shortest_path_snapshots


def main():
    map = """
    1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581
    """
    # Convert map to bit
    map = np.array(
        [list(line) for line in map.strip().replace(" ", "").split("\n")],
        dtype='uint8'
    )

    # Find shortest path
    dist_map, shortest_path = find_shortest_path(map, start=(0,0))

    # Animate
    fig, ax = plt.subplots()
    for i in range(len(dist_map)):
        ax.cla()
        ax.imshow(dist_map[i], vmin = dist_map[-1].min(), vmax=dist_map[-1].max())
        ax.plot(shortest_path[i][0], shortest_path[i][1], c='tab:red')
        plt.pause(0.001)
    plt.waitforbuttonpress()

if __name__ == "__main__":
    main()
