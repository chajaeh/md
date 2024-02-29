from collections import deque


def bfs(buslst2, buslst3, sx, sy, dx, dy, K):
    q = deque()

    visited = set()

    for i in range(1, K + 1):
        if (sx, sy) in buslst2[i]:
            q.append((i, (sx, sy), 0, {i}))

    while q:
        (curr, (cx, cy), cnt, visited) = q.popleft()
        if (cx, cy) == (dx, dy):
            return cnt
        for i in range(1, K + 1):
            for j in buslst3[i]:
                if (cx, cy) == j[1] and i not in visited:
                    for k in buslst3[i]:
                        if k[1] != (cx, cy):
                            q.append((k[0], k[1], cnt + 1, visited | {i}))


M, N = map(int, input().split())
K = int(input())
buslst = [[] for _ in range(K + 1)]

for i in range(1, K + 1):
    b, x1, y1, x2, y2 = map(int, input().split())
    buslst[b].append((x1, y1, x2, y2))

sx, sy, dx, dy = map(int, input().split())
buslst2 = [[] for _ in range(K + 1)]

for i in range(1, K + 1):
    [(x1, y1, x2, y2)] = buslst[i]

    buslst2[i].extend([(x, y1) for x in range(x1, x2 + 1)] + [(x1, y) for y in range(y1, y2 + 1)])

buslst3 = [[] for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, K + 1):
        if i != j:
            for (x1, y1) in buslst2[i]:
                for (x2, y2) in buslst2[j]:
                    if (x1, y1) == (x2, y2):
                        buslst3[i].append([j, (x1, y1)])

for i in range(1, K + 1):
    if (dx, dy) in buslst2[i]:
        buslst3[i].append((K + 1, (dx, dy)))

print(bfs(buslst2, buslst3, sx, sy, dx, dy, K))