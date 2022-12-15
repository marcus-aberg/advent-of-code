# aoc_template.py

import pathlib
import sys
import pprint


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    data = [d.split("->") for d in data]
    data = [[list(map(int, l.split(","))) for l in line] for line in data]

    return data


def generate_rocks(data):

    rocks = set()

    for d in data:
        for i in range(len(d) - 1):
            x1 = d[i][0]
            x2 = d[i + 1][0]
            y1 = d[i][1]
            y2 = d[i + 1][1]

            if (x2 - x1) != 0:
                rock = list(range(min(x1, x2), max(x1, x2) + 1))
                rock = [(r, y1) for r in rock]
            else:
                rock = list(range(min(y1, y2), max(y1, y2) + 1))
                rock = [(x1, r) for r in rock]

            rocks.update(rock)

    return rocks


def scan(pos, rocks):

    # Find all rocks directly underneath
    rocks_underneath = {r for r in rocks if r[0] == pos[0] and r[1] > pos[1]}

    return len(rocks_underneath) == 0


def part1(data):
    """Solve part 1."""

    rocks_and_sand = generate_rocks(data)

    directions = [(0, 1), (-1, 1), (1, 1)]
    falling_into_void = False
    units = 0

    while not falling_into_void:
        init = (500, 0)
        pos = init
        at_rest = False

        while not at_rest and not falling_into_void:
            moved = False

            for d in directions:
                next_pos = (pos[0] + d[0], pos[1] + d[1])

                if next_pos not in rocks_and_sand:
                    pos = next_pos
                    moved = True
                    break
                else:
                    continue

            at_rest = not moved

            if not at_rest:
                falling_into_void = scan(pos, rocks_and_sand)
            else:
                rocks_and_sand.add(pos)
                units += 1

    return units


def part2(data):
    """Solve part 2."""

    rocks_and_sand = generate_rocks(data)

    directions = [(0, 1), (-1, 1), (1, 1)]
    units = 0
    init = (500, 0)

    ymax = 0
    for r in rocks_and_sand:
        ymax = max(r[1], ymax)

    while init not in rocks_and_sand:
        pos = init
        at_rest = False

        while not at_rest:
            moved = False

            for d in directions:
                next_pos = (pos[0] + d[0], pos[1] + d[1])

                if next_pos[1] == (ymax + 2):
                    break

                elif next_pos not in rocks_and_sand:
                    pos = next_pos
                    moved = True
                    break

                else:
                    continue

            at_rest = not moved

            if at_rest:
                rocks_and_sand.add(pos)
                units += 1

    return units


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
