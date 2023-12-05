import re
import sys

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


def part_1(data: str):
    """
    Executes part 1 of the challenge.
    """

    return calibration_sum(data, PATTERN_PART_1)


def part_2(data: str):
    """
    Executes part 2 of the challenge.
    """

    return calibration_sum(data, PATTERN_PART_2)


def main(data_path: str):
    """
    Reads a file containing calibration values, calculates the sum of the values
    using different patterns, and prints the results.
    """

    with open(data_path, "r") as f:
        data = f.read().strip()

    print("Sum of calibration values:")
    print(f"• Part 1: {part_1(data)}")
    print(f"• Part 2: {part_2(data)}")


if __name__ == "__main__":
    main(data_path=sys.argv[1])
