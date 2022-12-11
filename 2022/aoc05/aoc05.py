# aoc_template.py

import pathlib
import sys


def move(stacks, instruction):
    for i in range(instruction["amount"]):
        stacks[instruction["to_stack"]].append(stacks[instruction["from_stack"]].pop())


def move2(stacks, instruction):
    amount = instruction["amount"]
    from_stack = instruction["from_stack"]
    to_stack = instruction["to_stack"]

    crates = stacks[from_stack][-amount:]
    stacks[from_stack] = stacks[from_stack][:-amount]
    stacks[to_stack] += crates


def parse(puzzle_input):
    """Parse input."""
    stacks_raw, instructions_raw = puzzle_input.split("\n\n")

    stacks_rows = stacks_raw.split("\n")
    indices = [i for i, c in enumerate(stacks_rows[-1]) if c != " "]
    stacks = [list() for i in range(len(indices))]
    for r in reversed(stacks_rows[0:-1]):
        for s, i in enumerate(indices):
            if r[i] != " ":
                stacks[s].append(r[i])

    instructions_rows = instructions_raw.split("\n")
    instructions = []
    for i_raw in instructions_rows:
        amount = int(i_raw.split(" ")[1])
        from_stack = int(i_raw.split(" ")[3]) - 1
        to_stack = int(i_raw.split(" ")[5]) - 1
        instructions.append(
            {"amount": amount, "from_stack": from_stack, "to_stack": to_stack}
        )

    return stacks, instructions


def part1(data):
    """Solve part 1."""
    stacks = data[0]
    instructions = data[1]

    for i in instructions:
        move(stacks, i)

    message = "".join([s[-1] for s in stacks])

    return message


def part2(data):
    """Solve part 2."""
    stacks = data[0]
    instructions = data[1]

    for i in instructions:
        move2(stacks, i)

    message = "".join([s[-1] for s in stacks])

    return message


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
