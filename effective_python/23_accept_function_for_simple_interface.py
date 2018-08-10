from collections import defaultdict


def log_missing():
    print("missing key.")
    return 0


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


if __name__ == '__main__':
    current = {'a': 1, 'd': 7}

    count_missing = CountMissing()
    result = defaultdict(count_missing)

    increments = [('c', 1), ('d', 5), ('r', 9)]
    for k, v in increments:
        result[k] += v

    print count_missing.added