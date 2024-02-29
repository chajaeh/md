import itertools

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1)]
subset = itertools.combinations(direction, 3)

print(*subset)
