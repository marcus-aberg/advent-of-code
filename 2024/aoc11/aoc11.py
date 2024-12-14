# aoc_template.py

import pathlib
import sys

from collections import defaultdict


def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input.split()


def blink(stones: list[str]):
    new_stones = []
    for stone in stones:
        new_stones += change(stone)

    return new_stones


def change(stone: str) -> list[str]:
    if stone == "0":
        return ["1"]
    if len(stone) % 2 == 0:
        n = int(len(stone) / 2)
        stone1 = stone[:n]
        stone2 = stone[n:].lstrip("0") or "0"
        return [stone1, stone2]
    return [str(int(stone) * 2024)]


def blink(stones: list[str]):
    new_stones = []
    for stone in stones:
        new_stones += change(stone)

    return new_stones


def part1(data):
    """Solve part 1."""
    stones = data
    for i in range(25):
        stones = blink(stones)

    return len(stones)


def part2(data):
    """Solve part 2."""
    orig_stones = defaultdict(int)
    for d in data:
        orig_stones[d] += 1

    for i in range(75):
        stones = defaultdict(int)
        for orig_s, count in orig_stones.items():
            for s in change(orig_s):
                stones[s] += count
        orig_stones = stones

    return sum(stones.values())


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
