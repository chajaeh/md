def dfs(arr, curr, end, vt):
    (y, x) = curr
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    vt.append(curr)
    if curr == end:
        return 1
    elif arr[y][x] == 1:
        return 0
    else:
        for dy, dx in direction:
            next_position = (y + dy, x + dx)
            if next_position not in vt and 0 <= y + dy < len(arr[0]) and 0 <= x + dx < len(arr[0]):
                if dfs(arr, next_position, end, vt):
                    return 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)
            if arr[i][j] == 3:
                end = (i, j)

    print(f'#{tc} {dfs(arr, start, end, [])}')
