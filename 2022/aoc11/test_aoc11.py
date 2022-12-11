# test_aoc_template.py

import pathlib
import pytest
import aoc11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

# TODO: Some problems have more than one example


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 10605


def test_part2_example1(example1):
    """Test part 2 on example input."""
    output = aoc.part2(example1)
    print(output)
    assert output == 2713310158


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
