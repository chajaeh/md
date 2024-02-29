from collections import deque

def bfs(adjl, sp, ep, K, N):
    global result
    q = deque()
    q.append(sp)
    vt = [sp]
    dt = [0] * (N+1)
    dt[sp] = 1
    while q:
        a = q.popleft()
        for i in adjl[a]:
            if i not in vt:
                q.append(i)
                vt.append(i)
                dt[i] = dt[a] + 1
    if dt[ep] <= K + 1:
        result += 1



N, M = map(int, input().split())
adjl = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
ep, K = map(int, input().split())
result = 0
for i in range(1, N+1):
    bfs(adjl, i, ep, K, N)
print(result)
