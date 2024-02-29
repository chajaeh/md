import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    goal = int(sys.stdin.readline())
    dq = deque()
    adjl = [[] for _ in range(N+1)]
    adjl2 = [[] for _ in range(N+1)]
    time = [0] * (N+1)
    for i in range(K):
        a, b = arr[i]
        adjl[a].append(b)
        adjl2[b].append(a)
    for i in range(1, N + 1):
        if len(adjl2[i]) == 0:
            dq.append(i)
            time[i] = D[i-1]
    while dq:
        a = dq.popleft()
        curr = a

        if curr == goal:
            print(time[curr])
            break
        else:
            if adjl[curr] != 0:
                for i in adjl[curr]:
                    time[i] = max(time[i], time[curr] + D[i - 1])
                    adjl2[i].remove(curr)
                    if len(adjl2[i]) == 0:
                        dq.append(i)

