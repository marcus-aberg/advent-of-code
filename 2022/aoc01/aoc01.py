# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    elves = puzzle_input.split("\n\n")
    calories = [e.split("\n") for e in elves]
    calories = [list(map(int, c)) for c in calories] # Convert to int 
    return calories

def part1(data):
    """Solve part 1."""
    calories_tot = [sum(d) for d in data]
    return max(calories_tot)

def part2(data):
    """Solve part 2."""
    calories_tot = [sum(d) for d in data]
    calories_tot.sort(reverse=True)
    return sum(calories_tot[0:3])

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
