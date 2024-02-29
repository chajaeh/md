import itertools

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

subsetlist = []
temp = itertools.combinations(numbers, 3)
subsetlist.extend(temp)
sumlist = []
for subset in subsetlist:
    if sum(subset) <= M:
        sumlist.append(sum(subset))

sumlist.sort(reverse=True)
print(sumlist[0])
