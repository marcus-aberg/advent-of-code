# aoc_template.py

import pathlib
import sys


def parse(puzzle_input: str):
    """Parse input."""
    return list(map(int, puzzle_input))


def part1(data: list[int]):
    """Solve part 1."""
    blocks = []
    id = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            blocks += [id] * d
            id += 1
        else:
            blocks += [-1] * d

    n = len(blocks)
    i = 0
    j = -1
    while i < n + j:
        if blocks[i] == -1:
            while blocks[j] == -1:
                j -= 1
            blocks[i] = blocks[j]
            blocks[j] = -1
        i += 1

    ans = 0
    for i, b in enumerate(blocks):
        if b != -1:
            ans += i * b

    return ans


def part2(data):
    """Solve part 2."""
    # Very slow solution, need to move the blocks as units instead somehow I guess xD
    # Or maybe enough to pre-allocate the lists
    blocks = []
    free_space = []
    id = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            blocks.append(d)
        else:
            free_space.append(d)

    n = len(blocks)
    file_system = []
    moved = []
    for i, (b, s) in enumerate(zip(blocks, free_space)):
        print(f"Filling space {i + 1} of {n}")
        file_system += [i] * b if i not in moved else [-1] * b
        space_left = s
        for j in [n - (k + 1) for k in range(n)]:
            if space_left == 0:
                break
            if j in moved:
                continue
            if j <= i:
                file_system += [-1] * space_left
                break
            if blocks[j] <= space_left:
                file_system += [j] * blocks[j]
                space_left -= blocks[j]
                moved += [j]

    ans = 0
    for i, b in enumerate(file_system):
        if b != -1:
            ans += i * b

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
