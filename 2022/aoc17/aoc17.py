# aoc_template.py

import pathlib
import sys
import time

import numpy as np


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.strip()


shapes = {
    "-": np.array([[1, 1, 1, 1]]),
    "+": np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    "L": np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
    "I": np.array([[1], [1], [1], [1]]),
    "[]": np.array([[1, 1], [1, 1]]),
    "O": np.array([[0] * 7] * 3),
    "B": np.array([[1] * 7]),
}


def check_collision(grid):
    return np.any(grid == 2)


def part1(data, n_rocks=2022):
    """Solve part 1."""
    # Initialize grid:
    grid = shapes["B"]
    rocks = ["-", "+", "L", "I", "[]"]
    jet_counter = 0

    t0 = time.time()
    log_interval = 2
    for n in range(n_rocks):
        if (time.time() - t0) >= log_interval:
            t0 = time.time()
            print(f"Current iteration: {n}")

        r = rocks[n % len(rocks)]
        rock = shapes[r]
        l_rock = rock.shape[1]
        h_rock = rock.shape[0]
        rock = np.pad(rock, ((0, 0), (2, 7 - l_rock - 2)))
        grid_tmp = np.concatenate((shapes["O"], grid))
        grid_tmp_tmp = grid_tmp.copy()
        i = 0
        overlap = 0
        while True:
            rock_prev = rock.copy()
            grid_tmp_prev = grid_tmp_tmp.copy()
            if i % 2 == 0:
                # Push left or right every second step
                push = data[jet_counter]
                if push == "<":
                    if any(rock[:, 0]):
                        # Do nothing if any part of the rock touches the left edge
                        pass
                    else:
                        rock = np.roll(rock, -1)
                elif push == ">":
                    if any(rock[:, -1]):
                        # Do nothing if any part of the rock touches the right edge
                        pass
                    else:
                        rock = np.roll(rock, 1)
                else:
                    raise Exception(f"Unknown push: {push}")

                jet_counter = (jet_counter + 1) % len(data)
            else:
                # Move down every other step
                overlap += 1

            # Merge and check for collision
            grid_tmp_tmp = grid_tmp.copy()
            if overlap != 0:
                grid_tmp_tmp[max(0, (overlap - h_rock)) : overlap, :] += rock[
                    -1 * min(h_rock, overlap) :, :
                ]

            if check_collision(grid_tmp_tmp):
                if i % 2 == 0:
                    # Continue if collision in horizontal direction and roll back rock movement
                    grid_tmp_tmp = grid_tmp_prev
                    rock = rock_prev
                    pass
                else:
                    # Stop rock if collision is in vertical direction and remove any empty lines at top
                    if h_rock > 3 and (overlap - 1) <= 3:
                        grid_tmp_prev = np.concatenate(
                            (rock[0 : (h_rock - 3), :], grid_tmp_prev)
                        )
                    grid = grid_tmp_prev[~np.all(grid_tmp_prev == 0, axis=1)]
                    break

            i += 1

    return grid.shape[0] - 1


def part2(data):
    """Solve part 2."""


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
