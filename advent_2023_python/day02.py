from __future__ import annotations
import re

COLORS = ["red", "green", "blue"]


class Round:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def from_string(s: str) -> Round:
        round = Round()
        matches = re.findall(r"(?P<num>\d+) (?P<color>\w+)", s)
        for match in matches:
            setattr(round, match[1], int(match[0]))
        return round

    def is_possible(self, maximum_colors: dict) -> bool:
        return (
            self.red <= maximum_colors["red"]
            and self.green <= maximum_colors["green"]
            and self.blue <= maximum_colors["blue"]
        )


class Game:
    number: int
    rounds: list[Round]

    def __init__(self):
        self.number = 0
        self.rounds = []

    @staticmethod
    def from_string(s: str) -> Game:
        game = Game()
        matches = re.match(r"Game (\d+):", s)
        if matches is None:
            raise ValueError(f"Invalid input; cannot parse game number: {s}")
        game.number = int(matches[1])
        rounds_string = s[len(matches[0]) :]
        for round in rounds_string.split(";"):
            game.rounds.append(Round.from_string(round))
        return game

    def is_possible(self, maximum_colors: dict) -> bool:
        for round in self.rounds:
            if not round.is_possible(maximum_colors):
                return False
        return True

    def minimum_power(self) -> int:
        return (
            max([round.red for round in self.rounds])
            * max([round.green for round in self.rounds])
            * max([round.blue for round in self.rounds])
        )


def part_1(data: str) -> int:
    max_colours = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for line in data.split("\n"):
        game = Game.from_string(line)
        if game.is_possible(max_colours):
            count += game.number
    return count


def part_2(data: str) -> int:
    count = 0
    for line in data.split("\n"):
        game = Game.from_string(line)
        count += game.minimum_power()
    return count


def main(data_path: str):
    with open(data_path, "r") as f:
        data = f.read().strip()

    print("Sum of calibration values:")
    print(f"• Part 1: {part_1(data)}")
    print(f"• Part 2: {part_2(data)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} DATA_PATH")
        sys.exit(1)
    main(data_path=sys.argv[1])
