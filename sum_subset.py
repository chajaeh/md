import itertools
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    value = 0
    subsetlist = []
    temp = itertools.combinations(numlist, N)
    subsetlist.extend(temp)
    for subset in subsetlist:
        if sum(subset) == K:
            value += 1
    print(f'{case} {value}')
