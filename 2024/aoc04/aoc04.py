# aoc_template.py

import pathlib
import sys
import re


def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def count_xmas(line: str, pattern=r"XMAS"):
    return len(re.findall(pattern, line))


def count_lines(lines: list[str], pattern=r"XMAS"):
    xmas_count = 0
    for line in lines:
        xmas_count += count_xmas(line, pattern)
        xmas_count += count_xmas(line[::-1], pattern)  # Revert line

    return xmas_count


def generate_diag_lines(data, reverse=False):
    diag_lines = []
    for i, row in enumerate(data):
        line = row if reverse else row[::-1]
        for j, l in enumerate(line):
            if len(diag_lines) < i + j + 1:
                diag_lines.append("")
            diag_lines[i + j] += l
    return diag_lines


def part1(data: list[str]):
    """Solve part 1."""
    # Horizontal
    horz_lines = data

    # Vertical
    vert_lines = ["".join(chars) for chars in zip(*data)]

    # Diagonal
    diag_lines = [generate_diag_lines(data, reverse=r) for r in [False, True]]

    ans = 0
    for lines in [horz_lines, vert_lines, *diag_lines]:
        ans += count_lines(lines)

    return ans


def count_x_mas(data):
    diag_lines = [generate_diag_lines(data, reverse=r) for r in [False, True]]

    ans = 0
    for lines in diag_lines:
        ans += count_lines(lines, pattern=r"MAS")

    return 1 if ans == 2 else 0


def part2(data):
    """Solve part 2."""
    ans = 0
    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            data_chunk = [d[j : j + 3] for d in data[i : i + 3]]
            ans += count_x_mas(data_chunk)

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
