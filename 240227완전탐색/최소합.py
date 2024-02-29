result = []
def dfs(N, arr, sp, sum):
    global result
    cy, cx = sp
    if cy == N-1 and cx == N-1:
        result.append(sum)
    if len(result) > 0 and sum > min(result):
        pass
    else:
        for dy, dx in direction:
            if 0 <= cy + dy < N and 0 <= cx + dx < N:
                dfs(N, arr, (cy + dy, cx + dx), sum + arr[cy + dy][cx + dx])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1,0), (0,1)]
    dfs(N, arr, (0, 0), arr[0][0])
    print(f'#{tc} {min(result)}')
    result = []