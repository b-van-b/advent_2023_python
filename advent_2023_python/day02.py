from __future__ import annotations
import re

COLORS = ["red", "green", "blue"]


class Round:
    """
    Represents cubes drawn in a single round of the game.

    red: number of red cubes
    green: number of green cubes
    blue: number of blue cubes
    """

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        """
        Initializes an instance of the class with the given values for red, green, and blue.

        Args:
            red (int): The number of red cubes. Defaults to 0.
            green (int): The number of green cubes. Defaults to 0.
            blue (int): The number of blue cubes. Defaults to 0.
        """
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def from_string(s: str) -> Round:
        """
        Parses a string into a Round object.

        Args:
            s (str): The string to parse.

        Returns:
            Round: The parsed Round object.
        """
        round = Round()
        matches = re.findall(r"(?P<num>\d+) (?P<color>\w+)", s)
        for match in matches:
            setattr(round, match[1], int(match[0]))
        return round

    def is_possible(self, maximum_colors: dict) -> bool:
        """
        Checks if the round is possible given the maximum number of each color.

        Args:
            maximum_colors (dict): A dictionary of the maximum number of each color.

        Returns:
            bool: True if the round is possible, False otherwise.
        """
        return (
            self.red <= maximum_colors["red"]
            and self.green <= maximum_colors["green"]
            and self.blue <= maximum_colors["blue"]
        )


class Game:
    """
    Represents a game of Cube Conundrum.

    number: game number
    rounds: list of rounds
    """
    number: int
    rounds: list[Round]

    def __init__(self):
        """
        Initializes an instance of the class.
        """
        self.number = 0
        self.rounds = []

    @staticmethod
    def from_string(s: str) -> Game:
        """
        Parses a string into a Game object.

        Args:
            s (str): The string to parse.

        Returns:
            Game: The parsed Game object.
        """
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
        """
        Checks if the game is possible given the maximum number of each color.

        Args:
            maximum_colors (dict): A dictionary of the maximum number of each color.

        Returns:
            bool: True if the game is possible, False otherwise.
        """
        for round in self.rounds:
            if not round.is_possible(maximum_colors):
                return False
        return True

    def minimum_power(self) -> int:
        """
        Calculates the minimum power of the game.

        Returns:
            int: The minimum power of the game.
        """
        return (
            max([round.red for round in self.rounds])
            * max([round.green for round in self.rounds])
            * max([round.blue for round in self.rounds])
        )


def part_1(data: str) -> int:
    """
    Executes part 1 of the challenge.
    """
    max_colours = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for line in data.split("\n"):
        game = Game.from_string(line)
        if game.is_possible(max_colours):
            count += game.number
    return count


def part_2(data: str) -> int:
    """
    Executes part 2 of the challenge.
    """
    count = 0
    for line in data.split("\n"):
        game = Game.from_string(line)
        count += game.minimum_power()
    return count


def main(data_path: str):
    """
    Reads a file containing game records and executes parts 1 and 2 of the challenge.

    Args:
        data_path (str): path to the data file
    """
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
