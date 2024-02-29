T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    pal = ''
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                pal = ''.join(arr[i][j:j+M])
    arr2 = [[row[i] for row in arr] for i in range(N)]
    for k in range(N):
        for l in range(N-M+1):
            if arr2[k][l:l+M] == arr2[k][l:l+M][::-1]:
                pal = ''.join(arr2[k][l:l+M])

    print(f'#{tc} {pal}')

