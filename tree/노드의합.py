T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heapq = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        heapq[a] = b
    i = 0
    while True:
        if 2 ** i > N:
            break
        else:
            i += 1
    i -= 1
    cur = 2**i
    while True:
        if cur == 1:
            break
        elif cur == N and cur % 2 == 0:
            heapq[cur//2] = heapq[cur]
            i -= 1
            cur = 2**i
        elif cur + 1 == N or cur + 2 == 2**(i+1):
            heapq[cur//2] = heapq[cur] + heapq[cur+1]
            i -= 1
            cur = 2**i
        else:
            heapq[cur//2] = heapq[cur] + heapq[cur+1]
            cur += 2
    print(f'#{tc} {heapq[L]}')


