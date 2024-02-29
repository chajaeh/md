T = int(input())

for case in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    viruslist = []
    direction = []
    for i in range(1, P+1):
        direction.append(tuple((0, i)))
        direction.append(tuple((0, -i)))
        direction.append(tuple((i, 0)))
        direction.append(tuple((-i, 0)))
    for y in range(N):
        for x in range(N):
            virus = 0
            virus += arr[y][x]

            for dy, dx in direction:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    virus += arr[ny][nx]
            viruslist.append(virus)

    print(f'#{case} {max(viruslist)}')

