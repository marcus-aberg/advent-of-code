# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input

def find_marker(data, buffer_length):
    for i, _ in enumerate(data[buffer_length-1:]):
        position = i + buffer_length
        if len(set(data[position-buffer_length:position])) == buffer_length:
            return position
    
    raise Exception("No marker found")
    
def part1(data):
    """Solve part 1."""
    return find_marker(data, buffer_length=4)
    
def part2(data):
    """Solve part 2."""
    return find_marker(data, buffer_length=14)

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
