# aoc_template.py

import pathlib
import sys

import copy

marker_direction_map: dict[str, tuple[int, int]] = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

markers = ["^", ">", "v", "<"]


def parse(puzzle_input: str) -> list[list[str]]:
    """Parse input."""
    lines = puzzle_input.splitlines()
    data = [list(line) for line in lines]
    return data


def part1(data: list[list[str]]):
    """Solve part 1."""
    # find starting position
    data, _ = walk(data)

    num_X = 0
    for row in data:
        num_X += row.count("X")

    return num_X


def walk(data):
    data = copy.deepcopy(data)  # Since we mutate the list
    position = find_starting_position(data)
    marker = get_symbol(data, position)
    inside = True
    steps = 0
    positions = set()
    while inside and (marker, position) not in positions:
        marker_start_index = markers.index(marker)
        positions.add((marker, position))
        for i in range(len(markers)):
            index = (marker_start_index + i) % len(markers)
            marker = markers[index]
            direction = marker_direction_map[marker]
            new_position = (
                position[0] + direction[0],
                position[1] + direction[1],
            )
            new_symbol = get_symbol(data, new_position)
            if new_symbol in ["#", "O"]:
                continue
            set_symbol(data, position, "X")
            if new_symbol == "OUTSIDE":
                inside = False
                break
            else:
                set_symbol(data, new_position, marker)
                position = new_position
                steps += 1
                break

    return data, inside


def print_data(data):
    for l in data:
        print(l)
    print("\n")


def get_symbol(data, position):
    dim = (len(data), len(data[0]))
    if not coord_in_grid(position, dim):
        return "OUTSIDE"

    symbol = data[position[0]][position[1]]
    return symbol


def set_symbol(data, position, symbol):
    dim = (len(data), len(data[0]))
    if not coord_in_grid(position, dim):
        raise ValueError("Position outside grid")

    data[position[0]][position[1]] = symbol


def coord_in_grid(coord: tuple[int, int], dim: tuple[int, int]):
    for c, d in zip(coord, dim):
        if not (0 <= c < d):
            return False

    return True


def find_starting_position(data: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in markers:
                return (i, j)

    raise LookupError("Starting position not found")


def part2(data):
    """Solve part 2."""
    ans = 0
    orig_data, _ = walk(data)
    start = find_starting_position(data)
    for i, row in enumerate(data):
        print(f"Testing row {i+1} of {len(data)}")
        for j, char in enumerate(row):
            if get_symbol(orig_data, (i, j)) == "X" and start != (i, j):
                set_symbol(data, (i, j), "O")
                _, inside = walk(data)
                ans += int(inside)
                set_symbol(data, (i, j), ".")

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
