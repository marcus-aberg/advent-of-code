# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str) -> list[list[int]]:
    """Parse input."""
    return [list(map(int, r.split())) for r in puzzle_input.splitlines()]


def all_increasing(row: list[int]) -> bool:
    return all(x > y for x, y in zip(row[1:], row))


def all_decreasing(row: list[int]) -> bool:
    return all(x < y for x, y in zip(row[1:], row))


def all_differs_allowed(row: list[int]) -> bool:
    return all(abs(x - y) <= 3 for x, y in zip(row[1:], row))


def row_is_ok(row):
    return all_differs_allowed(row) and (all_increasing(row) or all_decreasing(row))


def part1(data: list[list[int]]) -> int:
    """Solve part 1."""
    ans = 0
    for row in data:
        if row_is_ok(row):
            ans += 1

    return ans


def part2(data):
    """Solve part 2."""
    ans = 0
    for row in data:
        if row_is_ok(row):
            ans += 1
        else:
            for i in range(len(row)):
                reduced_row = row.copy()
                reduced_row.pop(i)
                if row_is_ok(reduced_row):
                    ans += 1
                    break

    return ans


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
