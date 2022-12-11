# aoc_template.py

import pathlib
import sys

import re
import time
import math


def parse(puzzle_input):
    """Parse input."""
    monkeys_raw = puzzle_input.split("\n\n")
    monkeys = []
    n_groups = 7
    regex = r"Monkey (\d*):\n\s+Starting items: (.+)\n\s+Operation: new = old ([\*\+]) (.+)\n\s+Test: divisible by (\d+)\n\s+If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)"

    for _, m in enumerate(monkeys_raw):
        match = re.search(regex, m)
        assert (
            len(match.groups()) == n_groups
        ), f"Length of monkey match should be {n_groups}"

        monkey = {}
        monkey["id"] = int(match.group(1))
        monkey["items"] = [int(i) for i in match.group(2).split(", ")]

        if match.group(3) == "*":
            if match.group(4) == "old":
                monkey["operation"] = lambda x: x * x
            else:
                factor = int(match.group(4))
                monkey["operation"] = lambda x, factor=factor: x * factor
        elif match.group(3) == "+":
            term = int(match.group(4))
            monkey["operation"] = lambda x, term=term: x + term
        else:
            raise Exception(f"Unknown operation: {match.group(3)}")
        divisor = int(match.group(5))
        monkey["test"] = lambda x, divisor=divisor: x % divisor == 0
        monkey["test_divisor"] = divisor
        monkey["if_true"] = int(match.group(6))
        monkey["if_false"] = int(match.group(7))
        # monkey["decrease_worry"] = lambda x: int(x / 3)
        monkey["inspections"] = 0

        monkeys.append(monkey)

    return monkeys


def do_round(i, monkeys, decrease_worry=lambda x: int(x / 3)):
    monkey = monkeys[i]
    items_to_remove = []
    for item in monkey["items"]:
        item_orig = item
        item = monkey["operation"](item)

        item = decrease_worry(item)

        if monkey["test"](item):
            monkeys[monkey["if_true"]]["items"].append(item)
            items_to_remove.append(item_orig)
        else:
            monkeys[monkey["if_false"]]["items"].append(item)
            items_to_remove.append(item_orig)
        monkey["inspections"] += 1

    for item in items_to_remove:
        monkey["items"].remove(item)


def part1(data):
    """Solve part 1."""
    monkeys = data
    rounds = 20

    for i in range(rounds):
        for i, _ in enumerate(monkeys):
            do_round(i, monkeys)

        # for m in monkeys:
        #    print(f"Monkey {m['id']}: {m['items']}")

    inspections = [m["inspections"] for m in monkeys]

    #    for n, i in enumerate(inspections):
    #        print(f"{n}: {i} inspections")
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


def part2(data):
    """Solve part 2."""
    monkeys = data
    print(monkeys)
    rounds = 10000

    t0 = time.time()

    divisors = [m["test_divisor"] for m in monkeys]
    decrease_worry = lambda x: x % math.prod(divisors)

    print(divisors)
    print(math.prod(divisors))

    for i in range(rounds):
        for i, _ in enumerate(monkeys):
            do_round(i, monkeys, decrease_worry=decrease_worry)

        # for m in monkeys:
        #    print(f"Monkey {m['id']}: {m['items']}")

    print(f"{rounds} rounds took {time.time() - t0} seconds wall time")

    inspections = [m["inspections"] for m in monkeys]

    for n, i in enumerate(inspections):
        print(f"Monkey {n} did {i} inspections")
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


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
        puzzle_input = (
            pathlib.Path(path).read_text().strip()
        )  # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
