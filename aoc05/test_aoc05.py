# test_aoc_template.py

import pathlib
import pytest
import aoc05 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [["Z","N"],["M","C","D"],["P"]]
    assert example1[1] == [{'amount': 1, 'from_stack': 1, 'to_stack': 0}, {'amount': 3, 'from_stack': 0, 'to_stack': 2}, {'amount': 2, 'from_stack': 1, 'to_stack': 0}, {'amount': 1, 'from_stack': 0, 'to_stack': 1}]
    
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == "CMZ"

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == "MCD"

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...