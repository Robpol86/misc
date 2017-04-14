#!/usr/bin/env python
"""Basic search algorithms."""

from pprint import pprint
from timeit import timeit

SORTED_DATA = [n + 10 for n in range(0, 100, 2)]  # [10, 12, ..., 108]


def builtin(needle, data=SORTED_DATA):
    """Use Python's built-in .find() method."""
    try:
        return data.index(needle)
    except ValueError:
        return -1


def linear(needle, data=SORTED_DATA):
    """Linear search."""
    # for i in range(len(data)):
    for i, value in enumerate(data):
        if value == needle:
            return i
    return -1


def binary(needle, data=SORTED_DATA):
    """Binary search."""
    start, end = 0, len(data) - 1
    while start <= end:
        middle = ((end - start) // 2) + start
        middle_value = data[middle]
        if middle_value == needle:
            return middle
        if needle < middle_value:
            end = middle - 1
        else:
            start = middle + 1
    return -1


def main():
    """Main function."""
    results = dict()
    number = 10000

    for func in ('builtin', 'linear', 'binary'):
        setup = 'from __main__ import %s as func' % func
        results[func] = timeit('assert func(78) == 34 and func(1000) == -1', setup=setup, number=number)

    pprint(sorted([(k, v) for k, v in results.items()], key=lambda p: p[1]))


if __name__ == '__main__':
    main()
