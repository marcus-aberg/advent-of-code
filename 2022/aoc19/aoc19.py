# aoc_template.py

import pathlib
import sys

import re


def parse(puzzle_input):
    """Parse input."""
    data = puzzle_input.split("\n")
    pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

    blueprints = []
    for d in data:
        match = re.search(pattern, d)
        b = {
            "id": int(match.group(1)),
            "bots": [
                {"name": "ore", "cost": {"ore": int(match.group(2))}},
                {"name": "clay", "cost": {"ore": int(match.group(3))}},
                {
                    "name": "obsidian",
                    "cost": {"ore": int(match.group(4)), "clay": int(match.group(5))},
                },
                {
                    "name": "geode",
                    "cost": {
                        "ore": int(match.group(6)),
                        "obsidian": int(match.group(7)),
                    },
                },
            ],
        }

        blueprints.append(b)

    return blueprints


def part1(data):
    """Solve part 1."""
    # Copy in data
    blueprints = data.copy()

    # Set number of minutes
    n_min = 24

    # Loop through all blueprints
    for b in blueprints:
        # Initialize new blueprint
        bot_fleet = {}
        stash = {}
        build_queue = {}
        for bot in b["bots"]:
            bot_fleet[bot["name"]] = 0
            stash[bot["name"]] = 0
            build_queue[bot["name"]] = 0

        bot_fleet["ore"] = 1

        # Loop through minutes
        for i in range(n_min):
            # Build new robots
            # TODO: I need a smart algo for building robots. Look up dynamic programming, possibly re-use day 16 sol.
            # NOTE: https://www.youtube.com/watch?v=bLMj50cpOug
            for bot in reversed(b["bots"]):
                build = True
                print(f"Build {bot['name']}?, Stash: {stash}")
                # Build current type as long as we have resources
                while build:
                    # Check if we have enough of all needed resources
                    for k, v in bot["cost"].items():
                        # If not do not build current type of bot
                        if stash[k] < v:
                            build = False

                    # If we have enough resources, pay price and add to build queue
                    if build:
                        build_queue[bot["name"]] += 1
                        for k, v in bot["cost"].items():
                            stash[k] -= v
                        print(f"Building {bot['name']}!, Stash: {stash}")

            # Collect resources
            for k, v in bot_fleet.items():
                stash[k] += v

            # Add new robots to fleet
            for k, v in build_queue.items():
                bot_fleet[k] += v
                build_queue[k] = 0

        # Log quality level
        b["quality_level"] = b["id"] * stash["geode"]

    # Return sum of all quality levels
    return sum([b["quality_level"] for b in blueprints])


def part2(data):
    """Solve part 2."""


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
