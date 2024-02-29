T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        if result == 'YES':
            break
        for j in range(N):
            if arr[i][j] == 'o':
                if i + 4 < N and all(arr[i+a][j] == 'o' for a in range(5)):
                    result = 'YES'
                    break
                if j + 4 < N and all(arr[i][j+a] == 'o' for a in range(5)):
                    result = 'YES'
                    break
                if i + 4 < N and j - 4 >= 0 and all(arr[i+a][j-a] == 'o' for a in range(5)):
                    result = 'YES'
                    break
                if i + 4 < N and j + 4 < N and all(arr[i+a][j+a] == 'o' for a in range(5)):
                    result = 'YES'
                    break
    print(f'#{tc} {result}')

