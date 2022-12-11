# test_aoc_template.py

import pathlib
import pytest
import aoc06 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "bvwbjplbgvbhsrlpgdmjqwftvncz"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 5


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == 6


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc.part1(example3) == 10


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc.part1(example4) == 11


def test_part2_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part2(example1) == 23


def test_part2_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part2(example2) == 23


def test_part2_example3(example3):
    """Test part 1 on example input."""
    assert aoc.part2(example3) == 29


def test_part2_example4(example4):
    """Test part 1 on example input."""
    assert aoc.part2(example4) == 26
