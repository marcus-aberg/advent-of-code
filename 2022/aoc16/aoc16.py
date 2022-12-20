# aoc_template.py

import pathlib
import sys

import re
import functools


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    pattern = r"Valve (.+) has flow rate=(.+); tunnel[s]? lead[s]? to valve[s]? (.+)"
    flows = {}
    neighbors = {}

    for d in data:
        match = re.search(pattern, d)
        valve_name = match.group(1)
        flow_rate = match.group(2)
        tunnel_valves = match.group(3).split(", ")
        flows[valve_name] = int(flow_rate)
        neighbors[valve_name] = tunnel_valves

    return flows, neighbors


def part1(data):
    """Solve part 1."""
    flows, neighbors = data

    sys.setrecursionlimit(6000)

    @functools.lru_cache(maxsize=None)
    def get_maximum(current, opened, min_left):
        if min_left <= 0:
            return 0

        best = 0

        # print(current, opened, min_left)
        for n in neighbors[current]:  # Traverse through all neighbors
            if (
                current not in opened and flows[current] != 0
            ):  # Open current valve if not opened and flow != 0
                val_if_open = (min_left - 1) * flows[current]
                opened_if_open = tuple(sorted(opened + (current,)))
                best = max(
                    best, val_if_open + get_maximum(n, opened_if_open, min_left - 2)
                )

            best = max(best, get_maximum(n, opened, min_left - 1))

        return best

    return get_maximum("AA", (), 30)


def part2(data):
    """Solve part 2."""
    flows, neighbors = data

    sys.setrecursionlimit(6000)

    @functools.lru_cache(maxsize=None)
    def get_maximum(current, opened, min_left):
        if min_left <= 0:
            return 0

        best = 0

        c1 = current[0]
        c2 = current[1]
        # print(current, opened, min_left)
        for n1 in neighbors[current[0]]:  # Traverse through all neighbors
            for n2 in neighbors[current[1]]:
                if c1 not in opened and flows[c1] != 0:
                    print("messa give up")


"""                 if current[0] not in opened and flows[current[0]] != 0: # Open current valve if not opened and flow != 0
                    val_if_open = (min_left - 1) * flows[current[0]]
                    opened_if_open = tuple(sorted(opened + (current[0], )))
                    best = max(best, val_if_open + get_maximum((n1, n2), opened_if_open, min_left - 2))
                
                if current[1] not in opened and flows[current[1]] != 0: # Open current valve if not opened and flow != 0
                    val_if_open = (min_left - 1) * flows[current[1]]
                    opened_if_open = tuple(sorted(opened + (current[1], )))
                    best = max(best, val_if_open + get_maximum((n1, n2), opened_if_open, min_left - 2))
                        
                best = max(best, get_maximum((n1, n2), opened, min_left - 1)) """

# return best

# return get_maximum(("AA", "AA"), (), 26)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:  # [r"./2022/aoc16/example1.txt"]: #sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = (
            pathlib.Path(path).read_text().strip()
        )  # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
