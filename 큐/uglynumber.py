import heapq

def ugly(n):
    q = []
    heapq.heappush(q, 1)
    for _ in range(n):
        a = heapq.heappop(q)
        b = a * 2
        c = a * 3
        d = a * 5
        if b not in q:
            heapq.heappush(q, b)
        if c not in q:
            heapq.heappush(q, c)
        if d not in q:
            heapq.heappush(q, d)
    return heapq.heappop(q)



Q = int(input())
lst = list(map(int, input().split()))
for i in lst:
    print(ugly(i-1), end=' ')



