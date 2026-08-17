import sys
import math
import json
import pathlib
import re
import statistics
from collections import Counter, defaultdict, deque

# Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Generator
def primes(limit):
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, int(math.sqrt(n)) + 1)):
            yield n

# Classes
class Dataset:
    def __init__(self, values):
        self.values = values

    @property
    def mean(self):
        return statistics.mean(self.values)

    def frequencies(self):
        return Counter(self.values)

data = Dataset([1, 2, 2, 3, 3, 3, 4, 5])

# JSON
payload = {
    "python": sys.version.split()[0],
    "fib_15": fib(15),
    "primes": list(primes(30)),
    "mean": data.mean,
    "frequencies": dict(data.frequencies()),
    "path": str(pathlib.Path.cwd()),
}

print(json.dumps(payload, indent=2))