from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #V 노드개수 E 간선정보수
    adjl = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjl[a-1].append(b)
        adjl[b-1].append(a)
    S, G = map(int, input().split())
    q = deque()
    q.append(S)
    vt = [S]
    dt = [0] * V
    while q:
        a = q.popleft()
        for i in adjl[a-1]:
            if i not in vt:
                q.append(i)
                vt.append(i)
                dt[i-1] = dt[a-1] + 1
    print(f'#{tc} {dt[G-1]}')
