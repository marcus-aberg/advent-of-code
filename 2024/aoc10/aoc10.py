# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str) -> list[list[int]]:
    """Parse input."""
    rows = puzzle_input.splitlines()
    return [list(map(int, r)) for r in rows]


def walk(start: tuple[int, int], data: list[list[int]]) -> set[tuple[int, int]]:
    up, down, left, right = (0, 1), (0, -1), (-1, 0), (1, 0)
    n = len(data)
    x, y = start
    nines_reached = set()
    if data[x][y] == 9:
        nines_reached.add((x, y))
        return nines_reached
    for dx, dy in [up, down, left, right]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < n:
            if data[xx][yy] - data[x][y] == 1:
                nines_reached.update(walk((xx, yy), data))

    return nines_reached


def walk2(start: tuple[int, int], data: list[list[int]]) -> int:
    up, down, left, right = (0, 1), (0, -1), (-1, 0), (1, 0)
    n = len(data)
    x, y = start
    if data[x][y] == 9:
        return 1
    score = 0
    for dx, dy in [up, down, left, right]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < n:
            if data[xx][yy] - data[x][y] == 1:
                score += walk2((xx, yy), data)

    return score


def part1(data: list[list[int]]):
    """Solve part 1."""
    # Find all starting places
    starting_places = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == 0:
                starting_places.append((i, j))

    # Do walk and calculate the score of each trailhead
    ans = 0
    for s in starting_places:
        nines = walk(s, data)
        score = len(nines)
        ans += score

    return ans


def part2(data):
    """Solve part 2."""
    # Find all starting places
    starting_places = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == 0:
                starting_places.append((i, j))

    # Do walk and calculate the score of each trailhead
    ans = 0
    for s in starting_places:
        score = walk2(s, data)
        ans += score

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
