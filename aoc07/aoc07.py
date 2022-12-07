# aoc_template.py

import pathlib
import sys

# My god this is terrible xD

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")

class Dir():
    def __init__(self, name):
        self.name = name
        self.content = []
    
    def get_size(self):
        """Get directory size"""
        sum = 0
        for c in self.content:
            sum+=c.get_size()
        
        return sum
    
    def add(self, item):
        """Adds item to directory content"""
        self.content.append(item)
        
    def get_subdirs(self):
        return [c for c in self.content if type(c) is Dir]
    
class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        """Get file size"""
        return self.size
        
def run_commands(commands):
    pwd = None
    cwd = None
    index = {}
    
    for i, c in enumerate(commands):
        #for k, dir in index.items():
            #content = [d.name for d in dir.content]
            #print(f"Cmd: {i} Key: {k} : {content}")
        words = c.split(" ")
        if words[1] == "cd":
            if words[2] == "..":
                cwd = "/".join(cwd.split("/")[:-1])
                cwd = "/" if cwd == "" else cwd
                continue
    
            if cwd is None:
                cwd = words[2]
            elif cwd == "/":
                pwd = cwd
                cwd = "".join((pwd, words[2]))
            else:
                pwd = cwd
                cwd = "/".join((pwd, words[2]))
            
            if cwd in index:
                continue
            else:
                dir = Dir(name=cwd)
                #print(f"Creating Dir! {dir.name} : {[i_d.name for i_d in dir.content]}")
                index[cwd] = dir
                if pwd is not None:
                    index[pwd].add(dir)

        
        if words[1] == "ls":
            continue
        
        if words[0].isnumeric():
            file = File(name=words[1], size=int(words[0]))
            index[cwd].add(file)
            
        if words[0] == "dir":
            continue # Will only work if we traverse all subdirs at some point
        
    return index        

def part1(data):
    """Solve part 1."""
    index = run_commands(data)        
    return sum([dir.get_size() for name, dir in index.items() if dir.get_size() <= 100000])
    
def part2(data):
    """Solve part 2."""
    index = run_commands(data)        
    total_space_used = index["/"].get_size()
    total_space = 70000000
    space_needed = 30000000
    min_size = total_space
    for name, dir in index.items():
        dir_size = dir.get_size()
        space_free_if_removed = total_space - total_space_used + dir_size
        if  space_free_if_removed > space_needed and dir_size < min_size:
            min_size = dir_size
        #print(f"total_space:{total_space} total_space_used:{total_space_used} space_free_if_removed:{space_free_if_removed} : dir_size:{dir_size} : min_size:{min_size}")
                         
    return  min_size

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input
                 )
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
