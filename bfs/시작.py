from collections import deque

def bfs(arr, N, sp):
    q = deque()
    q.append(sp)
    vt = [sp]
    while q:
        a = q.popleft()
        for i in range(N):
            if arr[a][i] == 1 and i not in vt:
                vt.append(i)
                q.append(i)
    return vt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(*bfs(arr,N,0))