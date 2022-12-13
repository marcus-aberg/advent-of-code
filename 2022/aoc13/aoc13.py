# aoc_template.py

import pathlib
import sys
import pprint


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n\n")
    data = [d.split("\n") for d in data]

    for pair in data:
        for i, p in enumerate(pair):
            exec("pair[i] = " + p)

    return data


def compare(left, right):
    # TODO: Cannot base to continue loop on passing an error, that is RIDICULOUS!
    # print(f"Compare {left} vs {right}")

    def _raise(l, r):
        raise Exception(f"Unknown state: l - {l}, r - {r}")

    for l, r in zip(left, right):  # Loop through left and right
        # print(f"Loop - Compare {l} vs {r}")
        type_left = type(l)
        type_right = type(r)

        # # print(l, r)
        # # print(type_left, type_right)

        if type_left is type_right:  # l and r is same type
            if type_left is int:
                if l < r:
                    # print(f"Left side is smaller (l:{l}, r:{r}), so inputs are in the right order")
                    return True

                elif l == r:
                    pass

                else:
                    # print(f"Right side is smaller (l:{l}, r:{r}), so inputs are not in the right order")
                    return False

            if type_left is list:
                try:
                    # print(f"Both are lists; expanding {l} vs {r} and retry comparison")
                    return compare(l, r)
                except:
                    pass  # Continue loop if we compare raises exception

        elif type_right is int:  # l and r is not same type and r is int
            try:
                # print(f"Mixed types; convert right to {[r]} and retry comparison")
                return compare(l, [r])
            except:
                pass  # Continue loop if we compare raises exception

        elif type_left is int:  # l and r is not same type and l is int
            try:
                # print(f"Mixed types; convert left to {[l]} and retry comparison")
                return compare([l], r)
            except:
                pass  # Continue loop if we compare raises exception

    if len(left) == len(right):  # Loop to end of list without returning, continue loop
        _raise(left, right)
    else:
        return len(left) < len(
            right
        )  # Left side ran out of items -> True, else -> False


def part1(data):
    """Solve part 1."""

    in_order = []
    for i, d in enumerate(data):
        if compare(left=d[0], right=d[1]):
            in_order.append(i + 1)

    # # print(in_order)

    return sum(in_order)


def part2(data):
    """Solve part 2."""
    # Mash all pairs together in long list
    packets = []
    # Append dividers
    divider1 = [[2]]
    divider2 = [[6]]

    packets.append(divider1)
    packets.append(divider2)

    for pair in data:
        for packet in pair:
            packets.append(packet)

    # Perform bubble-sort on the list based on compare
    for i in range(len(packets) - 1):
        # pprint.pp(packets)
        # print("\n")
        for j in range(len(packets) - 1):
            # # print(f"Comparing: {packets[j]} vs {packets[j + 1]}")
            if not compare(packets[j], packets[j + 1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    # pprint.pp(packets)
    # print("\n")

    id1 = packets.index(divider1) + 1
    id2 = packets.index(divider2) + 1

    return id1 * id2


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
