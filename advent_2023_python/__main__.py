# import importlib
from pathlib import Path
from collections.abc import Callable
import re

days: dict[int, Callable[[str], None]] = {}

try:
    import day01  # type: ignore

    days[1] = day01.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day02  # type: ignore

    days[2] = day02.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day03  # type: ignore

    days[3] = day03.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day04  # type: ignore

    days[4] = day04.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day05  # type: ignore

    days[5] = day05.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day06  # type: ignore

    days[6] = day06.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day07  # type: ignore

    days[7] = day07.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day08  # type: ignore

    days[8] = day08.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day09  # type: ignore

    days[9] = day09.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day10  # type: ignore

    days[10] = day10.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day11  # type: ignore

    days[11] = day11.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day12  # type: ignore

    days[12] = day12.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day13  # type: ignore

    days[13] = day13.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day14  # type: ignore

    days[14] = day14.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day15  # type: ignore

    days[15] = day15.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day16  # type: ignore

    days[16] = day16.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day17  # type: ignore

    days[17] = day17.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day18  # type: ignore

    days[18] = day18.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day19  # type: ignore

    days[19] = day19.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day20  # type: ignore

    days[20] = day20.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day21  # type: ignore

    days[21] = day21.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day22  # type: ignore

    days[22] = day22.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day23  # type: ignore

    days[23] = day23.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day24  # type: ignore

    days[24] = day24.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day25  # type: ignore

    days[25] = day25.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day26  # type: ignore

    days[26] = day26.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day27  # type: ignore

    days[27] = day27.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day28  # type: ignore

    days[28] = day28.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day29  # type: ignore

    days[29] = day29.main  # type: ignore
except ModuleNotFoundError:
    pass
try:
    import day30  # type: ignore

    days[30] = day30.main  # type: ignore
except ModuleNotFoundError:
    pass


def main():
    base_path = Path(__file__).resolve().parent
    module_path = base_path
    input_path = base_path / "input"

    # for file in module_path.iterdir():
    #     m = re.match(r"^day(\d+)\.py$", file.name)
    #     if m:
    #         day = int(m.group(1))
    #         print(f"Day {day}")
    #         print(file)
    #         module = importlib.import_module(str(file))
    #         module.main(input_path / f"day{day:02}.txt")
    print(days.keys())
    day = 0
    while day >= 0:
        day = int(input("Which day? "))
        if day in days:
            days[day](str(input_path / f"day{day:02}.txt"))
        else:
            print(f"Day {day} not found")


if __name__ == "__main__":
    main()
