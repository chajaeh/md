from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = deque()
    lst = list(map(int, input().split()))
    for i in lst:
        q.append(i)
    for j in range(M):
        a = q.popleft()
        q.append(a)
    print(f'#{tc} {q.popleft()}')

#lst = deque(map(int, input().split()))
#lst.rotate(-M)