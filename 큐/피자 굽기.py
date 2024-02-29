from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = deque()
    lst = list(map(int, input().split()))
    dict = {}
    mylst = []
    for i in range(M):
        dict[i+1] = lst[i]
        mylst.append(i+1)
    for j in range(N):
        q.append(mylst[j])
    mylst = mylst[N:]
    while True:
        a = q.popleft()
        dict[a] = dict[a] // 2
        if dict[a] == 0 and len(mylst) >= 1:
            q.append(mylst[0])
            mylst = mylst[1:]
        elif dict[a] == 0 and len(mylst) == 0:
            pass
        else:
            q.append(a)
        if len(q) == 1:
            break
    b = q[0]
    print(f'#{tc} {b}')


#pizzas = deque([[i+1, p]] for i, p in enumrate(cheeses)
