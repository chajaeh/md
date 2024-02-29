T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    white = [(N//2, N//2), (N//2 + 1, N//2 + 1)]
    black = [(N//2 + 1, N // 2), (N // 2, N // 2 + 1)]
    direction = [(1, 1), (1,0), (-1, 0), (0,1),(0,-1),(1,-1),(-1,1),(-1,-1)]
    for x, y, color in arr:
        if color == 1:
            for dx, dy in direction:
                if (x + dx, y + dy) in white:
                    for i in range(1, N):
                        if (x + dx * i, y + dy * i) not in black and (x + dx * i, y + dy * i) not in white:
                            break
                        if (x + dx * i, y + dy * i) in black:
                            for j in range(0, i):
                                if (x + dx * j, y + dy * j) in white:
                                    white.remove((x + dx * j, y + dy * j))
                                    black.append((x + dx * j, y + dy * j))
                            break
            black.append((x, y))
        else:
            for dx, dy in direction:
                if (x + dx, y + dy) in black:
                    for i in range(1, N):
                        if (x + dx * i, y + dy * i) not in black and (x + dx * i, y + dy * i) not in white:
                            break
                        if (x + dx * i, y + dy * i) in white:
                            for j in range(0, i):
                                if (x + dx * j, y + dy * j) in black:
                                    black.remove((x + dx * j, y + dy * j))
                                    white.append((x + dx * j, y + dy * j))
                            break
            white.append((x, y))
    print(black)
    print(white)
    print(f'#{tc} {len(black)} {len(white)}')
