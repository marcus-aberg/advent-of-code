# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    data = [int(i) for i in puzzle_input.split("\n")]
    return data


def part1(data):
    """Solve part 1."""
    r = list(zip(data.copy(), range(len(data))))

    for i in range(len(data)):
        # print([rr[0] for rr in r])
        # Find index of current iterate
        idx = 0
        while r[idx][1] != i:
            idx += 1

        item = r.pop(idx)

        insert_idx = (idx + item[0]) % len(r)
        if insert_idx == 0:
            r.append(item)
        else:
            r.insert(insert_idx, item)

    # Find 0
    idx_0 = [rr[0] for rr in r].index(0)
    indices = [i + idx_0 for i in [1000, 2000, 3000]]
    values = [r[i % (len(r))][0] for i in indices]
    # print(values)
    # print([rr[0] for rr in r])
    ret_sum = sum(values)

    return ret_sum


def mix(data, times=10):
    r = list(zip(data.copy(), range(len(data))))

    for _ in range(times):
        for i in range(len(data)):
            # print([rr[0] for rr in r])
            # Find index of current iterate
            idx = 0
            while r[idx][1] != i:
                idx += 1

            item = r.pop(idx)

            insert_idx = (idx + item[0]) % len(r)
            if insert_idx == 0:
                r.append(item)
            else:
                r.insert(insert_idx, item)

    return [rr[0] for rr in r]
    # Keep track of position in new list


def part2(data):
    """Solve part 2."""
    decryption_key = 811589153
    data = [decryption_key * d for d in data]
    data = mix(data, 10)

    idx_0 = data.index(0)
    indices = [i + idx_0 for i in [1000, 2000, 3000]]
    values = [data[i % (len(data))] for i in indices]
    # print(values)
    # print(data)
    ret_sum = sum(values)

    return ret_sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
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
