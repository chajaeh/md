T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    squarelist = []
    for i in range(N):
        for j in range(N):
            startpoint = arr[i][j]
            for k in range(i, N):
                for l in range(j, N):
                    if startpoint == arr[k][l]:
                        endpoint = arr[k][l]
                        squarelist.append((k - i + 1)*(l - j +1))
    maxarea = max(squarelist)
    print(f'#{case} {squarelist.count(maxarea)}')
