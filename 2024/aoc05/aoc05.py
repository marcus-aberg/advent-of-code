# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    [rules_raw, lines_raw] = puzzle_input.split("\n\n")
    rules = [
        list(
            map(
                int,
                rule.split("|"),
            )
        )
        for rule in rules_raw.splitlines()
    ]

    lines = [
        list(
            map(
                int,
                line.split(","),
            )
        )
        for line in lines_raw.splitlines()
    ]

    return (rules, lines)


def line_correct(line: list[int], rules: list[list[int]]):
    for i, l in enumerate(line):
        # find rules that has l as 1st index
        for rule in rules:
            if l == rule[0]:
                # check that 1st index of rule is before 2nd index in the list
                if rule[1] in line[:i]:
                    return False

    return True


def correct_line(line: list[int], rules: list[list[int]]):
    line = line.copy()
    for i, l in enumerate(line):
        # find rules that has l as 1st index
        for rule in rules:
            if l == rule[0]:
                if rule[1] in line[:i]:
                    old_index = line.index(rule[0])
                    new_index = line.index(rule[1])
                    item = line.pop(old_index)
                    line.insert(new_index, item)
                    return correct_line(line, rules)

    return line


def part1(data: tuple[list[list[int]], list[list[int]]]):
    """Solve part 1."""
    (rules, lines) = data
    ans = 0
    for line in lines:
        if line_correct(line, rules):
            ans += line[len(line) // 2]

    return ans


def part2(data):
    """Solve part 2."""
    (rules, lines) = data
    ans = 0
    for line in lines:
        if not line_correct(line, rules):
            corrected_line = correct_line(line, rules)
            ans += corrected_line[len(corrected_line) // 2]

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
