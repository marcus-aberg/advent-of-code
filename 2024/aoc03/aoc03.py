# aoc_template.py

import pathlib
import sys
import re


def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input


def part1(data: str):
    """Solve part 1."""
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    ans = 0
    for m in matches:
        ans += int(m[0]) * int(m[1])

    return ans


def part2(data):
    """Solve part 2."""
    pattern = r"(do)\(\)|(don't)\(\)|(mul)\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    ans = 0
    enabled = True
    for m in matches:
        if m[0]:
            enabled = True
        if m[1]:
            enabled = False
        if m[2] and enabled:
            ans += int(m[3]) * int(m[4])

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
