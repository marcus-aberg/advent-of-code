# aoc_template.py

import pathlib
import sys

import numpy as np


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    data = [d.split(" ") for d in data]
    data = [[d[0], int(d[1])] for d in data]

    return data


direction_map = {
    "U": np.array([1, 0]),
    "D": np.array([-1, 0]),
    "L": np.array([0, -1]),
    "R": np.array([0, 1]),
}


def part1(data):
    """Solve part 1."""
    H = np.array([0, 0])
    T = np.array([0, 0])
    T_p = set([str(T)])

    for move in data:
        direction = move[0]
        n_steps = move[1]

        for s in range(n_steps):
            step = direction_map[direction]
            H += step
            H_prior = H - step
            if max(np.abs(H - T)) >= 2:
                T += H_prior - T

                T_p.add(str(T))

    return len(T_p)


def part2(data):
    """Solve part 2."""
    tail_length = 9
    H = np.array([0, 0])
    T = np.array([[0, 0]] * tail_length)
    T_end_p = set([str(T[-1])])

    for move in data:
        direction = move[0]
        n_steps = move[1]

        for s in range(n_steps):
            step = direction_map[direction]
            H += step
            for i, t in enumerate(T):
                t_ahead = H if i == 0 else T[i - 1]
                t_hat = t_ahead - t  # Array from ahead point to this point
                if max(np.abs(t_hat)) >= 2:  # Not adjacent
                    t += np.sign(
                        t_hat
                    )  # Move at most 1 in each direction towards t_ahead

            T_end_p.add(str(T[-1]))

    return len(T_end_p)


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
