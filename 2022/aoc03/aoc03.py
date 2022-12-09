# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    items = puzzle_input.split("\n")
    rucksacks = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in items]
    return rucksacks

def get_prio(c):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    prio = alphabet.index(c.lower())+ 1 + c.isupper()*26
    return prio

def part1(data):
    """Solve part 1."""
    common_items = ["".join(set(d[0]).intersection(set(d[1]))) for d in data]
    prios = [get_prio(c) for c in common_items]
    return sum(prios)     

def part2(data):
    """Solve part 2."""
    all_items = ["".join(set(d[0]).union(set(d[1]))) for d in data]
    groups = [all_items[i:i+3] for i in range(0,len(all_items), 3)]
    badges = ["".join(set(g[0]).intersection(set(g[1]), set(g[2]))) for g in groups]
    prios = [get_prio(b) for b in badges]
    return sum(prios)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
