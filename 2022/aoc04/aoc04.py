# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    pairs = puzzle_input.split("\n")

    def transform_pair(pair):
        ret_list = []
        for p in pair.split(","):
            nums = p.split("-")
            ret_list.append(set(range(int(nums[0]), int(nums[1]) + 1)))

        return ret_list

    pairs = [transform_pair(p) for p in pairs]

    return pairs


def part1(data):
    """Solve part 1."""
    fully_contained = [d[0].issubset(d[1]) or d[1].issubset(d[0]) for d in data]
    return sum(fully_contained)


def part2(data):
    """Solve part 2."""
    overlaps = [d[0].intersection(d[1]) != set() for d in data]
    return sum(overlaps)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
