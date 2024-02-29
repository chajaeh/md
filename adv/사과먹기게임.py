T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxval = 0
    for i in range(N):
        for j in range(N):
            maxval = max(maxval, arr[i][j])
    k = 1
    apple = [(0, 0)]
    while k <= maxval:
        for a in range(N):
            for b in range(N):
                if arr[a][b] == k:
                    apple.append((a, b))
        k += 1
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    turn = 0
    curr = direction[turn % 4]
    c = 0
    while c < maxval:
        y, x = apple[c]
        ny, nx = apple[c+1]
        if turn % 4 == 0:
            if ny > y and nx > x:
                c += 1
                turn += 1
                continue
            elif ny > y and nx < x:
                c += 1
                turn += 2
                continue
            else:
                c += 1
                turn += 3
                continue
        elif turn % 4 == 1:
            if ny > y and nx < x:
                c += 1
                turn += 1
                continue
            elif ny < y and nx < x:
                c += 1
                turn += 2
                continue
            else:
                c += 1
                turn += 3
                continue
        elif turn % 4 == 2:
            if ny < y and nx < x:
                c += 1
                turn += 1
                continue
            elif ny < y and nx > x:
                c += 1
                turn += 2
                continue
            else:
                c += 1
                turn += 3
                continue
        elif turn % 4 == 3:
            if ny < y and nx > x:
                c += 1
                turn += 1
                continue
            elif ny > y and nx > x:
                c += 1
                turn += 2
                continue
            else:
                c += 1
                turn += 3
                continue

    print(f'#{tc} {turn}')
