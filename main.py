import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

nice = {(1, 3), (9, 8), (8, 0), (2, 1), (0, 3), (7, 2), (1, 2), (3, 6), (1, 1), (3, 2),
        (8, 2), (3, 9), (0, 5), (1, 0), (3, 5), (5, 3), (4, 6), (3, 8), (0, 9)}


def generate_cells(n=5, r=10):
    return {(random.randrange(r), random.randrange(r)) for _ in range(n)}


def get_neighbours(tup):
    positions = [-1, 1, 0]
    return {(tup[0] + a, tup[1] + b) for a in positions for b in positions if tup != (tup[0] + a, tup[1] + b)}


def get_range():
    x = {a[0] for a in cells}
    x.update({a[1] for a in cells})
    low = min(x) - 5
    high = max(x) + 5
    return low, high


def life(i):
    global go, cells, future_alive, future_dead, ax
    if go:
        cells -= future_dead
        cells.update(future_alive)
        future_dead = set()
        future_alive = set()
        go = len(cells) > 0

        for cell in cells:
            for neighbour in get_neighbours(cell):
                if len(get_neighbours(neighbour) & cells) == 3:
                    future_alive.add(neighbour)
            if len(get_neighbours(cell) & cells) not in [2, 3]:
                future_dead.add(cell)

        print(cells)
        ax.clear()
        plt.axis('equal')
        ax.scatter(*zip(*cells), marker='s', s=800)


if __name__ == '__main__':
    cells = generate_cells(60, 10)

    future_alive = set()
    future_dead = set()
    go = True

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    anim = FuncAnimation(fig, life, interval=200)
    plt.show()

time.sleep(10)
