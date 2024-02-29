from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    q = deque()
    maxval = lst[-1]
    if lst.count(maxval) == N:
        print(f'#{tc} 0')
        continue

    for i in range(N):
        lst[i] -= maxval
        lst[i] = abs(lst[i])
        if lst[i] != 0:
            q.append(lst[i])
    d = 1

    while q:
        a = q.popleft()
        water = 2 - (d % 2)
        if water == 1:
            if len(q) == 0 and a == 2:
                d += 1
                q.append(a)
                continue
            else:
                if all(q[i] % 2 == 0 for i in range(len(q))) and a % 2 == 0:
                    a -= 1
                    d += 1
                    q.append(a)
                    continue
                else:
                    if a % 2 == 0:
                        q.append(a)
                        continue
                    else:
                        a -= 1
                        d += 1
                        if a != 0:
                            q.append(a)
                        continue

        elif water == 2:
            if a == 1 and len(q) == 0:
                q.append(a)
                d += 1
                continue
            if a > 1:
                a -= 2
                d += 1
                if a != 0:
                    q.append(a)
                continue
            else:
                q.append(a)
                continue
        q.append(a)
        d += 1
    print(f'#{tc} {d - 1}')





