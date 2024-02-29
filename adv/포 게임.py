import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
eaten_jjol = []
def dfs(arr, N, direc, po, moved):
    global eaten_jjol
    temparr = deepcopy(arr)
    if moved == 3:
        return
    for (dy, dx) in direc:
        (cy, cx) = po
        if 0 <= dy+cy < N and 0 <= dx + cx < N:
            if dx == 0:
                cnt = 0
                if dy < 0:
                    for i in range(1, abs(dy)):
                        if arr[cy - i][cx] == 1:
                            cnt += 1
                        if cnt == 2:
                            break
                    if cnt == 1:
                        if temparr[cy + dy][cx] == 1:
                            if (cy + dy, cx) not in eaten_jjol:
                                eaten_jjol.append((cy+dy, cx))
                            temparr[cy + dy][cx] = 0
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy+ dy, cx), moved+1)
                            temparr[cy+dy][cx] = 1
                            temparr[cy][cx] = 2
                        elif temparr[cy + dy][cx] == 0:
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy+dy, cx), moved+1)
                            temparr[cy][cx] = 2
                elif dy > 0:
                    for i in range(1, abs(dy)):
                        if arr[cy + i][cx] == 1:
                            cnt += 1
                        if cnt == 2:
                            break
                    if cnt == 1:
                        if temparr[cy + dy][cx] == 1:
                            if (cy+dy, cx) not in eaten_jjol:
                                eaten_jjol.append((cy+dy, cx))
                            temparr[cy + dy][cx] = 0
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy+dy, cx), moved+1)
                            temparr[cy + dy][cx] = 1
                            temparr[cy][cx] = 2
                        elif temparr[cy + dy][cx] == 0:
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy+dy, cx), moved+1)
                            temparr[cy][cx] = 2
            if dy == 0:
                cnt = 0
                if dx < 0:
                    for i in range(1, abs(dx)):
                        if arr[cy][cx - i] == 1:
                            cnt += 1
                        if cnt == 2:
                            break
                    if cnt == 1:
                        if temparr[cy][cx + dx] == 1:
                            if (cy, cx + dx) not in eaten_jjol:
                                eaten_jjol.append((cy, cx + dx))
                            temparr[cy][cx + dx] = 0
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy, cx + dx), moved+1)
                            temparr[cy][cx + dx] = 1
                            temparr[cy][cx] = 2
                        elif temparr[cy][cx + dx] == 0:
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy, cx + dx), moved+1)
                            temparr[cy][cx] = 2
                elif dx > 0:
                    for i in range(1, abs(dx)):
                        if arr[cy][cx + i] == 1:
                            cnt += 1
                        if cnt == 2:
                            break
                    if cnt == 1:
                        if temparr[cy][cx + dx] == 1:
                            if (cy, cx + dx) not in eaten_jjol:
                                eaten_jjol.append((cy, cx + dx))
                            temparr[cy][cx + dx] = 0
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy, cx + dx), moved+1)
                            temparr[cy][cx + dx] = 1
                            temparr[cy][cx] = 2
                        elif temparr[cy][cx + dx] == 0:
                            temparr[cy][cx] = 0
                            dfs(temparr, N, direc, (cy, cx + dx), moved+1)
                            temparr[cy][cx] = 2











T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direc = []
    for i in range(1, N):
        direc.append((i, 0))
        direc.append((-i, 0))
        direc.append((0, i))
        direc.append((0, -i))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                po = (i, j)

    dfs(arr, N, direc, po, 0)
    print(f'#{tc} {len(eaten_jjol)}')
    eaten_jjol = []



