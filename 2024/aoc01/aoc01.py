# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str) -> list[list[int]]:
    """Parse input."""
    rows = puzzle_input.split("\n")
    data = [list(map(int, r.split("   "))) for r in rows]
    return data


def part1(data):
    """Solve part 1."""
    l1 = sorted([r[0] for r in data])
    l2 = sorted([r[1] for r in data])

    diffs = [abs(a - b) for a, b in zip(l1, l2)]

    ans = sum(diffs)

    return ans


def part2(data):
    """Solve part 2."""
    l1 = [r[0] for r in data]
    l2 = [r[1] for r in data]

    sim_scores = [a * l2.count(a) for a in l1]

    ans = sum(sim_scores)

    return ans


def solve(puzzle_input):
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
