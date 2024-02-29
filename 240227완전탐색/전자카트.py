result = []

def dfs(N, arr, sp, sum, vt):
    global result
    if len(vt) == N - 1:
        result.append(sum + arr[sp][0])
    for i in range(1, N):
        if i not in vt:
            dfs(N, arr, i, sum + arr[sp][i], vt+[i])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dfs(N, arr, 0, 0, [])
    print(f'#{tc} {min(result)}')
    result = []