from advent_2023_python.day02 import Game, Round, part_1, part_2
import pytest


class TestRoundInit:
    def test_by_arguments(self):
        round = Round(456, 0, 0)
        assert round.red == 456
        assert round.green == 0
        assert round.blue == 0

    def test_default(self):
        round = Round()
        assert round.red == 0
        assert round.green == 0
        assert round.blue == 0


class TestRoundFromString:
    def test_one_color(self):
        round = Round.from_string("456 green")
        assert round.red == 0
        assert round.green == 456
        assert round.blue == 0

    def test_two_colors(self):
        round = Round.from_string("3 blue, 4 red")
        assert round.red == 4
        assert round.green == 0
        assert round.blue == 3

    def test_three_colors(self):
        round = Round.from_string("8 green, 6 blue, 20 red")
        assert round.red == 20
        assert round.green == 8
        assert round.blue == 6


class TestGameInit:
    def test_default(self):
        game = Game()
        assert game.number == 0
        assert len(game.rounds) == 0


class TestGameFromString:
    def test_three_rounds(self):
        game = Game.from_string(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        assert game.number == 3
        assert len(game.rounds) == 3
        assert game.rounds[0].green == 8
        assert game.rounds[0].blue == 6
        assert game.rounds[0].red == 20
        assert game.rounds[1].green == 13
        assert game.rounds[1].blue == 5
        assert game.rounds[1].red == 4
        assert game.rounds[2].green == 5
        assert game.rounds[2].blue == 0
        assert game.rounds[2].red == 1

    def test_no_game_number(self):
        with pytest.raises(ValueError):
            Game.from_string(
                "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
            )


class TestGamePossibility:
    def test_possible(self):
        game = Game.from_string(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        maximum_colors = {"red": 20, "green": 17, "blue": 6}
        assert game.is_possible(maximum_colors)

    def test_impossible(self):
        game = Game.from_string(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        maximum_colors = {"red": 20, "green": 17, "blue": 5}
        assert game.is_possible(maximum_colors) == False


class TestPart1:
    def test_one(self):
        assert (
            part_1(
                "Game 1: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
            )
            == 0
        )

    def test_two(self):
        assert (
            part_1(
                """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
            )
            == 8
        )


class TestGameMinumumPower:
    def test_one(self):
        assert (
            Game.from_string(
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
            ).minimum_power()
            == 48
        )

    def test_two(self):
        assert (
            Game.from_string(
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
            ).minimum_power()
            == 12
        )


class TestPart2:
    def test_one(self):
        assert part_2("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48

    def test_two(self):
        assert (
            part_2(
                """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
            )
            == 2286
        )
