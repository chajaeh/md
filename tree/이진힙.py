from copy import deepcopy
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    heapq = [0] * (N+1)
    node = 1
    for i in lst:
        cur = deepcopy(node)
        heapq[cur] = i
        while True:
            if cur//2 == 0 or heapq[cur//2] < heapq[cur]:
                break
            else:
                heapq[cur//2], heapq[cur] = heapq[cur], heapq[cur//2]
                cur //= 2
        node += 1
    sum = 0
    N //= 2
    while True:
        if N == 0:
            break
        else:
            sum += heapq[N]
            N //= 2

    print(f'#{tc} {sum}')