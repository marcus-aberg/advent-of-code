# aoc_template.py

import pathlib
import sys

import re

def parse(puzzle_input):
    """Parse input."""
    data_raw = puzzle_input.split("\n")
    
    pattern = r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)"
    data = []
    for d in data_raw:
        groups = list(map(int, re.search(pattern, d).groups()))
        assert len(groups) == 4
        s = (groups[0], groups[1])
        b = (groups[2], groups[3])
        data.append({'s': s, 'b': b})
    
    return data
        
def distance(p1, p2):
    # Manhattan Distance
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def add_distance(data):
    for d in data:
        d['d'] = distance(d['s'], d['b'])

def scan_row(y, data):
    covered = set()
    for d in data:
        p_closest = (d['s'][0], y)
        x_closest = d['s'][0]
        d_p_closest = distance(d['s'], p_closest)
        overlap = d['d'] - d_p_closest
        
        if overlap >= 0:
            x_covered = [x + x_closest for x in list(range(-overlap, overlap + 1))]
            p_covered = [(x, y) for x in x_covered if (x,y) != d['b']] 
            covered.update(p_covered)
    
    return(covered)
                
        
def part1(row, data):
    """Solve part 1."""
    add_distance(data)
    covered = scan_row(row, data)
    
    return len(covered)


def scan_p(p, data):
    # Return True if covered
    for d in data:
        p_distance = distance(d['s'], p)
        if p_distance <= d['d']:
            return True
        
    return False    
    
def part2(maxi, data):
    """Solve part 2."""
    
    add_distance(data)
    
    directions = [(-1, 0), (1, 0)]
    pos_lines = []
    neg_lines = []
    
    for s in data:
        sx = s['s'][0]
        sy = s['s'][1]
        bd = s['d']
        
        for d in directions:
            dx = d[0]
            dy = d[1]
            px = sx + dx*bd
            py = sy + dy*bd
            
            neg_lines.append(py + px)
            pos_lines.append(py - px)
        
    nl = len(data) * 2
    for i in range(nl):
        for j in range(i + 1, nl):
            n1, n2 = neg_lines[i], neg_lines[j]

            if abs(n2 - n1) == 2:
                nmin = min(n1, n2) + 1
            
            p1, p2 = pos_lines[i], pos_lines[j]
            if abs(p2 - p1) == 2:
                pmin = min(p1, p2) + 1 
    
    dx = (nmin - pmin) // 2
    dy = (nmin + pmin) // 2
    
    return dx*4000000 + dy
            

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(2000000, data)
    solution2 = part2(4000000, data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = (
            pathlib.Path(path).read_text().strip()
        )  # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
