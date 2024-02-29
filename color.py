T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for squares in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 +1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
    purple = 0
    for k in range(10):
        for l in range(10):
            if arr[k][l] == 3:
                purple += 1
    print(f'#{case} {purple}')



