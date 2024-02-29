arr = [['_'] * 5 for _ in range(4)]
for _ in range(2):
    y,x = map(int, input().split())
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny > 3 or nx> 4:
            continue
        arr[ny][nx] = '#'
for row in arr:
    print(*row)

direction = [(-1,-1) ....]
for dy, dx in direction
    ny= y+dy
    nx = x + dx