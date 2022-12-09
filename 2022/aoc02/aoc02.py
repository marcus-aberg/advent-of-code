# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    rounds = puzzle_input.split("\n")
    rounds = [r.split(" ") for r in rounds]
    
    return rounds 

def part1(data):
    """Solve part 1."""
    def get_round_point(round):
        if round[1] == "X":
            points = 1
            if round[0] == "A":
                return points + 3   
            elif round[0] == "B":
                return points + 0
            elif round[0] == "C": 
                return points + 6 
        elif round[1] == "Y":
            points = 2
            if round[0] == "A":
                return points + 6   
            elif round[0] == "B":
                return points + 3
            elif round[0] == "C":
                return points + 0
        elif round[1] == "Z":
            points = 3
            if round[0] == "A":   
                return points + 0
            elif round[0] == "B":
                return points + 6
            elif round[0] == "C":
                return points + 3
            
    round_points = [get_round_point(d) for d in data]
    
    return sum(round_points)
        

def part2(data):
    """Solve part 2."""
    def get_round_point(round):
        if round[1] == "X":
            points = 0
            if round[0] == "A":
                return points + 3   
            elif round[0] == "B":
                return points + 1
            elif round[0] == "C": 
                return points + 2 
        elif round[1] == "Y":
            points = 3
            if round[0] == "A":
                return points + 1   
            elif round[0] == "B":
                return points + 2
            elif round[0] == "C":
                return points + 3
        elif round[1] == "Z":
            points = 6
            if round[0] == "A":   
                return points + 2
            elif round[0] == "B":
                return points + 3
            elif round[0] == "C":
                return points + 1
            
    round_points = [get_round_point(d) for d in data]

    return sum(round_points)
            
    round_points = [get_round_point(d) for d in data]
    
    return sum(round_points)
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
