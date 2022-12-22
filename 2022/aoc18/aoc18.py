# aoc_template.py

import pathlib
import sys

import numpy as np
from collections import deque


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    data = [np.array(list(map(int, d.split(",")))) for d in data]

    return data


def part1(data):
    """Solve part 1."""
    data = data.copy()

    exposed = 0
    for d in data:
        for i in (0, 1, 2):
            for r in (-1, 1):
                dir = np.zeros(3, dtype=int)
                dir[i] = r
                side = d + dir
                if not np.any(np.all(side == data, axis=1)):
                    exposed += 1

    return exposed


def part2(data):
    """Solve part 2."""
    # Copy input data
    data = data.copy()

    # -- Create 3d matrix --
    # Find out dimensions of matrix
    x_dim = 0
    y_dim = 0
    z_dim = 0
    for d in data:
        x_dim = max(x_dim, d[0])
        y_dim = max(y_dim, d[1])
        z_dim = max(z_dim, d[2])

    # Create matrix with zeros
    # Pad with edge of len = 1 to be able to do search on edge (+2)
    mat = np.zeros((x_dim + 2, y_dim + 2, z_dim + 2), dtype=int)
    mat_min = (0, 0, 0)
    mat_max = (x_dim + 1, y_dim + 1, z_dim + 1)

    # Give all indices where a rock exists value 1
    for d in data:
        mat[tuple(d)] = 1

    # -- Find all non-cavities using bfs --
    # We should be able to reach all non-cavities if we:
    #   - Pad our matrix with 0 all around
    #   - Start at index which is on the edge and not a rock

    start = (0, 0, 0)  # is on edge and is not a rock as it is in the padding
    # visited = list()
    queue = list()

    # visited.append(start)
    mat[start] = -1
    queue.append(start)

    while queue:  # Is not empty

        s = queue.pop()

        adjacent = []
        for i in (0, 1, 2):
            for j in (-1, 1):
                d = [0, 0, 0]
                d[i] = j
                a = tuple((sum((ss, dd)) for ss, dd in zip(s, d)))

                # Check if inside mat and is not a stone and not visited:
                if (
                    all([mat_min[ai] <= av <= mat_max[ai] for ai, av in enumerate(a)])
                    and mat[a] == 0
                ):
                    adjacent.append(a)

        for a in adjacent:
            if mat[a] != -1:
                mat[a] = -1
                # visited.append(a)
                queue.append(a)

    # Go through all stones and check how many edges touches a non-cavity
    exposed = 0
    for d in data:
        for i in (0, 1, 2):
            for r in (-1, 1):
                dir = np.zeros(3, dtype=int)
                dir[i] = r
                side = d + dir
                if mat[tuple(side)] == -1:
                    exposed += 1

    return exposed


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = (
            pathlib.Path(path).read_text().strip()
        )  # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
