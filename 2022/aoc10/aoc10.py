# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    data = [d.split(" ") for d in data]
    data = [[d[0], int(d[1])] if len(d) == 2 else d for d in data]
    return data


def part1(data):
    """Solve part 1."""
    x = 1
    i = 0
    processing = False
    signal_strengths = []
    cycle = 0
    while i < len(data):
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal_strengths.append(cycle * x)
            # print(cycle, x, signal_strengths[-1])
        else:
            pass  # print(cycle, x)

        ins = data[i][0]

        if ins == "addx":
            if processing == False:
                processing = True
                v = data[i][1]
            else:
                processing = False
                x += +v
                i += 1
        elif ins == "noop":
            i += 1

    return sum(signal_strengths)


def part2(data):
    """Solve part 2."""
    x = 1
    i = 0
    processing = False
    cycle = 0
    carriage_position = 0
    printout = ""
    while i < len(data):
        cycle += 1
        ins = data[i][0]
        sprite_position = set([x, x + 1, x - 1])
        if carriage_position in sprite_position:
            printout += "#"
        else:
            printout += "."

        carriage_position += 1

        if carriage_position % 40 == 0:
            printout += "\r\n"
            carriage_position = 0

        if ins == "addx":
            if processing == False:
                processing = True
                v = data[i][1]
            else:
                processing = False
                x += +v
                i += 1
        elif ins == "noop":
            i += 1

    print(printout)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = (
            pathlib.Path(path).read_text().strip()
        )  # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
