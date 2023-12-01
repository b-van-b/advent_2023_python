import pytest
from advent_2023_python.day01 import (
    calibration_value,
    calibration_sum,
    PATTERN_PART_1,
    PATTERN_PART_2,
)


LINES_PART_1 = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
]
BLOCK_PART_1 = (
    "\n".join([line[0] for line in LINES_PART_1]),
    sum(line[1] for line in LINES_PART_1),
)

LINES_PART_2 = [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
]
BLOCK_PART_2 = (
    "\n".join([line[0] for line in LINES_PART_2]),
    sum(line[1] for line in LINES_PART_2),
)


def test_part_1():
    for line in LINES_PART_1:
        assert calibration_value(line[0], PATTERN_PART_1) == line[1]

    assert calibration_sum(BLOCK_PART_1[0], PATTERN_PART_1) == BLOCK_PART_1[1]


def test_part_2_with_part_1_values():
    for line in LINES_PART_1:
        assert calibration_value(line[0], PATTERN_PART_2) == line[1]

    assert calibration_sum(BLOCK_PART_1[0], PATTERN_PART_2) == BLOCK_PART_1[1]


def test_part_2_with_part_2_values():
    for line in LINES_PART_2:
        assert calibration_value(line[0], PATTERN_PART_2) == line[1]

    assert calibration_sum(BLOCK_PART_2[0], PATTERN_PART_2) == BLOCK_PART_2[1]


def test_no_digits():
    with pytest.raises(ValueError):
        calibration_value("abc", PATTERN_PART_1)

    with pytest.raises(ValueError):
        calibration_value("abc", PATTERN_PART_2)
