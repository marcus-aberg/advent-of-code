# aoc_template.py

import pathlib
import sys

from itertools import product
import operator


def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))


operators = [operator.add, operator.mul, concatenate]


def parse(puzzle_input: str):
    """Parse input."""
    lines = puzzle_input.splitlines()
    data = []
    for line in lines:
        answer_raw, terms_raw = line.split(":")
        answer = int(answer_raw)
        terms = tuple(map(int, terms_raw.split()))
        data.append((answer, terms))

    return data


def part1(data: list[tuple[int, tuple[int]]]):
    """Solve part 1."""
    return calibrate(data, operators=operators[:2])


def calibrate(data, operators):
    ans = 0
    for equation in data:
        answer, terms = equation
        operator_permutations = product(operators, repeat=len(terms) - 1)
        for operator_permutation in operator_permutations:
            acc = terms[0]
            for i in range(len(terms) - 1):
                acc = operator_permutation[i](acc, terms[i + 1])
            if acc == answer:
                ans += answer
                break

    return ans


def part2(data):
    """Solve part 2."""
    return calibrate(data, operators=operators)


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
