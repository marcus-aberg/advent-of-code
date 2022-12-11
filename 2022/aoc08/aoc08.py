# aoc_template.py

import pathlib
import sys

import numpy


def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.split("\n")
    rows = [list(map(int, r)) for r in rows]
    return numpy.array(rows)


def is_visible(idx, x, data):
    i, j = (idx[0] + 1, idx[1] + 1)
    v_l = all(x > data[i, :j])
    v_r = all(x > data[i, j + 1 :])
    v_a = all(x > data[:i, j])
    v_b = all(x > data[i + 1 :, j])
    if any([v_l, v_r, v_a, v_b]):
        return True


def part1(data):
    """Solve part 1."""
    shape = data.shape
    visible = 2 * shape[0] + 2 * shape[1] - 4
    for idx, x in numpy.ndenumerate(data[1:-1, 1:-1]):
        if is_visible(idx, x, data):
            visible += 1

    return visible


def get_view_score(x, trees_in_direction):
    visible_trees = numpy.where(x <= trees_in_direction)[0] + 1
    if len(visible_trees) == 0:
        visible_trees = len(trees_in_direction)
    else:
        visible_trees = visible_trees[0]

    return visible_trees


def part2(data):
    """Solve part 2."""
    max_view_score = 0
    for idx, x in numpy.ndenumerate(data[1:-1, 1:-1]):
        if is_visible(idx, x, data):
            i, j = (idx[0] + 1, idx[1] + 1)
            d_l = get_view_score(x, numpy.flip(data[i, :j]))
            d_r = get_view_score(x, data[i, j + 1 :])
            d_a = get_view_score(x, numpy.flip(data[:i, j]))
            d_b = get_view_score(x, data[i + 1 :, j])
            cur_view_score = d_l * d_r * d_a * d_b
            if cur_view_score > max_view_score:
                max_view_score = cur_view_score

    return max_view_score


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
