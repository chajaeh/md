from collections import deque

N, M = map(int, input().split()) # N 지역수, M 관계수
adjl = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
T = int(input())
adjl[T] = []
vt = []
vt.append(1)
q = deque()
q.append(1)
dt = [0] * (N+1)

while q:
    a = q.popleft()
    for i in adjl[a]:
        if i not in vt:
            q.append(i)
            vt.append(i)
            dt[i] = dt[a] + 1

print(dt[N])