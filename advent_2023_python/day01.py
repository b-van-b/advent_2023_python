import re
from pathlib import Path


DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    r"\d",
]

PATTERN_PART_1 = r"\d"
PATTERN_PART_2 = f"(?=({'|'.join(DIGITS)}))"


def get_digit(s: str) -> int:
    """Return the digit in the input

    Args:
        s (str): one string containing a single digit represented by a single arabic numeral or spelled out in lower-case English

    Returns:
        int: the digit as an integer value
    """

    try:
        return int(s)
    except ValueError:
        return DIGITS.index(s)


def calibration_value(line: str, pattern: str) -> int:
    """Return the calibration value in the input

    Args:
        line (str): one line containing a calibration value
        pattern (str): the regular expression pattern to match

    Raises:
        ValueError: if no digits are found in the line

    Returns:
        int: the calibration value
    """

    digits = re.findall(pattern, line)

    if digits:
        return get_digit(digits[0]) * 10 + get_digit(digits[-1])

    raise ValueError(f"No digits found in: '{line}'")


def calibration_sum(lines: str, pattern: str) -> int:
    """Return the sum of the calibration values in the input

    Args:
        lines (str): one or more lines containing calibration values

    Returns:
        int: the sum of the calibration values
    """

    sum = 0

    for line in lines.split("\n"):
        sum += calibration_value(line, pattern)

    return sum


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input" / "day01.txt"

    lines = path.read_text().strip()

    print("Sum of calibration values:")
    print(f"• Part 1: {calibration_sum(lines, PATTERN_PART_1)}")
    print(f"• Part 2: {calibration_sum(lines, PATTERN_PART_2)}")
