for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    t = 0
    while t <= 102:
        for i in range(N):
            for j in range(N):
                a = arr[i][j]
                if a == 1:
                    if 0 <= i + 1 < N and arr[i+1][j] == 0:
                        arr[i][j] = 0
                        arr[i+1][j] = 1
                    elif i + 1 == N:
                        arr[i][j] = 0
                elif a == 2:
                    if 0 <= i - 1 < N and arr[i-1][j] == 0:
                        arr[i][j] = 0
                        arr[i-1][j] = 2
                    elif i == 0:
                        arr[i][j] = 0
        t += 1
    cnt = 0

    st = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr[i][j] = 0
                for k in range(1, N):
                    if arr[i+k][j] == 2:
                        arr[i+k][j] = 0
                        cnt += 1
                        break
                    else:
                        arr[i+k][j] = 0

    print(f'#{tc} {cnt}')