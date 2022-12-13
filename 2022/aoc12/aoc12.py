# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    
    return data

def height(n):
    
    if n == "S":    
        n = "a"
        
    elif n == "E":    
        n = "z"
        
    else:
        n = n
    
    return ord(n) - 96

def construct_graph(data):
    
    nodes = {}    
    surroundings = [[-1, 0],
                   [1, 0],
                   [0, -1],
                   [0, 1]]
        
    for i, row in enumerate(data):
        
        for j, loc in enumerate(row):
            
            n = {} 
            n["h"] = loc 
            n["children"] = []
            
            for s in surroundings:
                
                sr = i + s[0]
                sc = j + s[1]
                
                if sr >= 0 and sc >= 0 and sr <= (len(data) - 1) and sc <= (len(row) - 1): # Inside matrix
                    
                    if (height(data[sr][sc]) - height(loc)) <= 1: # Allowed step - TODO: I probably want to prioritize search directions that lead upward
                        
                        n["children"].append((sr, sc))
                        
            nodes[i, j] = n
            
    return nodes

def find_start_end(data):
    
    S = False
    E = False
    
    for i, row in enumerate(data):
        
        for j, loc in enumerate(row):
            
            if loc == "S":
                
                S = (i, j)
            
            if loc == "E":
                
                E = (i, j)

            if S and E:
                
                return  S, E
                
def find_indices(s, data, matches=-1):
    
    indices = []
    
    for i, row in enumerate(data):
        
        for j, loc in enumerate(row):
            
            if loc == s:
                
                indices.append((i, j))
            
            if len(indices) == matches:
                
                return indices
                
    return indices
            
def construct_priority_queue(S, nodes):
    
    # Create priority queue
    large_number = 1e60
    priority_queue = [] # Add start node at top of queue
    
    for key in nodes:
        
        if key == S:
        
            priority_queue.insert(0, {"id": S, "length": 0, "prior": None})
        
        # else:
            
        #    priority_queue.append({"id": key, "length": large_number, "prior": None})
    
    return priority_queue    

def find_shortest_path(S, E, data):
    
    # Create needed data structures for Dijkstra's
    nodes = construct_graph(data)
    priority_queue = construct_priority_queue(S, nodes)
    sort_criteria = lambda d: d["length"]
    
    visited = []
    
    while True:
        
        if len(priority_queue) == 0:
            
            return []
        
        else:
            current = priority_queue.pop(0) # Pop from top of list
            visited.append(current)
        
        if current["id"] == E: # Goal: When E is on top of your priority queue and E is "popped" ->  this is when we have finished the algorithm 
            
            break
        
        for child in nodes[current["id"]]["children"]:
            
            if len([v for v in visited if v["id"] == child]) != 0: # If we already visited this node - TODO: Improve this to not have to search every time
                
                continue
            
            child_item = next((i for i in priority_queue if i["id"] == child), None)            
            child_length = current["length"] + 1
            
            if child_item is None: # Unseen node
                
                # print(f"Appending: {child}")
                queue_item = {"id": child, "length": child_length, "prior": current}    # TODO: Maybe I can add some heuristic to improve the search direction
                priority_queue.append(queue_item)
                
            else: # Seen node
                
                if child_item["length"] > child_length:
                
                    child_item["length"] = child_length
                    child_item["prior"] = current
                    
                else:
                    
                    pass
        
        priority_queue.sort(key = sort_criteria) # TODO: Maybe I can insert the nodes in the priority-queue properly instead of sorting it every time
    
    # Construct path backwards        
    shortest_path = []
    shortest_path.append(visited[-1])
    
    while shortest_path[-1] is not None:
        
        shortest_path.append(shortest_path[-1]["prior"])
        
    return shortest_path
            
def part1(data):
    """Solve part 1."""
    S, E = find_start_end(data)
    shortest_path = find_shortest_path(S, E, data)
    end = shortest_path[0]
    return end["length"]
    
def part2(data):
    """Solve part 2."""
    
    E = find_indices("E", data, matches=1)[0]
    starts = find_indices("a", data)
    
    length = 1e60
    
    for i, S in enumerate(starts):
        
        print(f"Start: {i + 1}")
        
        shortest_path = find_shortest_path(S, E, data)
        
        if len(shortest_path) > 0:
            end = shortest_path[0]
            length = min(end["length"], length)
            print(f"Start: {i + 1} - shortest path: {length}")
        else: 
            print(f"Start: {i + 1} - no shortest path found!")
        
    assert length != 1e60, "No paths found!"
    
    return length

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip() # TODO: For some problems strip() is inefficient, spaces might be significant
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
