#!/usr/bin/env python
"""Basic search algorithms."""

from __future__ import print_function

import sys
from pprint import pprint
from random import randint, uniform
from timeit import timeit

HOSTS = {
    'serverA': 1,
    'serverB': 2,
    'serverC': 2,
    'serverD': 2,
    'serverE': 2,
    'serverF': 2,
    'serverG': 2,
    'serverH': 2,
    'serverI': 2,
    'serverJ': 2,
    'serverK': 2,
    'serverL': 5,
}


class Linear(object):
    """Simple linear search approach."""

    def __init__(self):
        self.sum = sum(HOSTS.values())

    def __call__(self, worst_case=False):
        if worst_case:
            rand = self.sum
        else:
            rand = uniform(0, self.sum)
        for host, weight in HOSTS.items():
            if weight >= rand:
                return host
            rand -= weight


class Hash(object):
    """Hash table approach."""

    def __init__(self):
        self.servers = dict()
        self.ceil = 0
        for server, weight in HOSTS.items():
            assert weight > 0
            self.ceil += weight
            self.servers[self.ceil] = server

    def __call__(self, worst_case=False):
        if worst_case:
            rand = 0
        else:
            rand = randint(0, self.ceil)
        while True:
            if rand in self.servers:
                return self.servers[rand]
            else:
                rand += 1


def main():
    """Main function."""
    results = dict()

    # First run multiple times and print counts to verify algorithms work.
    for cls in ('Linear', 'Hash'):
        func = globals()[cls]()
        for _ in range(200):
            host = func()
            if host not in results:
                results[host] = 1
            else:
                results[host] += 1
        print(cls)
        pprint(sorted([(k, v) for k, v in results.items()], key=lambda p: p[0]))
        print()
        results.clear()
    sys.stdout.flush()

    # Next compare worst case time complexities.
    number = 10000
    for cls in ('Linear', 'Hash'):
        setup = 'from __main__ import %s as cls; func = cls()' % cls
        results[cls] = timeit('assert func(True)', setup=setup, number=number)

    pprint(sorted([(k, v) for k, v in results.items()], key=lambda p: p[1]))


if __name__ == '__main__':
    main()
