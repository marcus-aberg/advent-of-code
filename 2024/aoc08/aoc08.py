# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data: list[str]):
    """Solve part 1."""
    # Find all frequencies and their positions
    frequencies: dict[str, list[tuple[int, int]]] = {}
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char != ".":
                if not frequencies.get(char):
                    frequencies[char] = []
                frequencies[char].append((x, y))

    # For each position, go through all other of the same frequency and log the "reflection"
    reflections = set()
    x_max = len(data[0]) - 1
    y_max = len(data[1]) - 1
    for frequency, positions in frequencies.items():
        for i, a in enumerate(positions):
            for j, b in enumerate(positions):
                if i != j:
                    r = (2 * a[0] - b[0], 2 * a[1] - b[1])  # Reflection formula
                    # For each reflection check that it is inside the grid.
                    if 0 <= r[0] <= x_max and 0 <= r[1] <= y_max:
                        # If so add it to a set (only unique reflections count)
                        reflections.add(r)

    return len(reflections)


def part2(data: list[str]):
    """Solve part 2."""
    # Find all frequencies and their positions
    frequencies: dict[str, list[tuple[int, int]]] = {}
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char != ".":
                if not frequencies.get(char):
                    frequencies[char] = []
                frequencies[char].append((x, y))

    # For each position, go through all other of the same frequency and log the "reflection"
    reflections = set()
    x_max = len(data[0]) - 1
    y_max = len(data[1]) - 1
    for frequency, positions in frequencies.items():
        for i, a in enumerate(positions):
            for j, b in enumerate(positions):
                if i != j:
                    n = 0
                    while True:
                        r = (
                            (n + 1) * a[0] - n * b[0],
                            (n + 1) * a[1] - n * b[1],
                        )  # Reflection formula
                        # For each reflection check that it is inside the grid.
                        if 0 <= r[0] <= x_max and 0 <= r[1] <= y_max:
                            # If so add it to a set (only unique reflections count) and increment n
                            reflections.add(r)
                            n += 1
                        else:
                            # Else we are outside and don't need to calculate more points
                            break

    return len(reflections)


def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        # TODO: For some problems strip() is dangerous if spaces matters
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
