"""
Avoid unpacking more than three return values by returning a small data object.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import median
from typing import Iterable


@dataclass(frozen=True)
class Stats:
    minimum: float
    maximum: float
    average: float
    median: float
    count: int


def get_stats(values: Iterable[float]) -> Stats:
    """
    Return summary statistics for the provided numbers.

    The caller receives a Stats instance instead of a long tuple, which keeps the
    unpacking on the caller side simple and explicit.
    """
    numbers = list(values)
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = sum(numbers)
    count = len(numbers)
    return Stats(
        minimum=min(numbers),
        maximum=max(numbers),
        average=total / count,
        median=median(numbers),
        count=count,
    )


def get_avg_ratio(values: Iterable[float]) -> list[float]:
    """Return ratios that express each value relative to the average."""
    numbers = list(values)
    if not numbers:
        raise ValueError("numbers must not be empty")

    average = sum(numbers) / len(numbers)
    scaled = [value / average for value in numbers]
    scaled.sort(reverse=True)
    return scaled


def show_unpacking_examples() -> None:
    """Demonstrate unpacking with short tuples and starred expressions."""

    def my_function() -> tuple[int, int]:
        return 1, 2

    first, second = my_function()
    assert first == 1
    assert second == 2

    lengths = [12, 42, 342, 355, 23, 66, 835, 21, 2]
    longest, *middle, shortest = get_avg_ratio(lengths)
    print(f"longest: {longest:>4.0%}")
    print(f"shortest: {shortest:>4.0%}")
    print(f"middle ratios: {middle}")


"""
TTR:
    1. you can have functions return multiple values by putting them ina  tuple and having hte caller
    take advantage of python's unpacking syntax
    2. multiple return values from a function can also be unpacekd by catch-all starred expressions
    3. unpacking into for our more vars is error prone and should be avoided, instead, return a small class or
    namedtuple instance
"""
