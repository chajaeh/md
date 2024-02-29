T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    maxval = lst[-1]
    if lst.count(maxval) == N:
        print(f'#{tc} 0')
        continue
    for i in range(N):
        lst[i] -= maxval
        lst[i] = abs(lst[i])
    d = 1
    while True:
        water = 2 - (d % 2)
        if water == 1:
            for i in range(N):
                if i == N - 1 and lst.count(0) == N-1 and lst.count(2) == 1:
                    break

                if lst[i] % 2 == 1:
                    lst[i] -= water
                    break

                elif i == N -1 and lst[i] >= 1:
                    lst[i] -= water
                    break
                elif i == N - 1 and lst[i] == 0:
                    for j in range(N):
                        if lst[j] > 0:
                            lst[j] -= water
                            break

        elif water == 2:
            for i in range(N):
                if lst[i] > 1:
                    lst[i] -= water
                    break
        if all(lst[j] == 0 for j in range(N)):
            break
        d += 1
    print(f'#{tc} {d}')