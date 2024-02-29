import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy
def move(N, sp, direction, curdirec, arr, dct):
    [i, j] = sp
    if canmove(N, sp, direction, curdirec, arr, dct):
        if curdirec == [0, 1]:
            ny = i + 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'down'
            ny = i
            nx = j + 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'right'
            ny = i - 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'up'
            ny = i
            nx = j - 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'left'
        elif curdirec == [1, 0]:
            ny = i
            nx = j - 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'left'
            ny = i + 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'down'
            ny = i
            nx = j + 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'right'
            ny = i - 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'up'
        elif curdirec == [0, -1]:
            ny = i - 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'up'
            ny = i
            nx = j - 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'left'
            ny = i + 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'down'
            ny = i
            nx = j + 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'right'
        elif curdirec == [-1, 0]:
            ny = i
            nx = j + 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'right'
            ny = i - 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'up'
            ny = i
            nx = j - 1
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'left'
            ny = i + 1
            nx = j
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5):
                return 'down'





def canmove(N, sp, direction, curdirec, arr, dct):
    [i, j] = sp
    for [dy, dx] in direction:
        ny = i + dy
        nx = j + dx
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0 or arr[ny][nx] > dct[(ny, nx)] + 5:
                return 1


def robot(N, M, sp, dct, direction, curdirec, arr):
    day = 0
    cnt = 0
    [i, j] = sp
    while day <= M -1:
        for k in range(N):
            for l in range(N):
                if arr[k][l] >= 2:
                    arr[k][l] += 1
        if arr[i][j] == 0 and canmove(N, [i, j], direction, curdirec, arr, dct):
            dct[(i, j)] += 1
            arr[i][j] = 2
            if move(N, [i, j], direction, curdirec, arr, dct) == 'up':
                i -= 1
                curdirec = [-1, 0]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'down':
                i += 1
                curdirec = [1, 0]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'left':
                j -= 1
                curdirec = [0, -1]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'right':
                j += 1
                curdirec = [0, 1]
        elif not canmove(N, [i, j], direction, curdirec, arr, dct):
            if arr[i][j] > 5 + dct[(i, j)]:
                cnt += 1
                arr[i][j] = 0
            else:
                pass
        elif arr[i][j] > 5 + dct[(i, j)]:
            arr[i][j] = 0
            cnt += 1
            if move(N, [i, j], direction, curdirec, arr, dct) == 'up':
                i -= 1
                curdirec = [-1, 0]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'down':
                i += 1
                curdirec = [1, 0]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'left':
                j -= 1
                curdirec = [0, -1]
            elif move(N, [i, j], direction, curdirec, arr, dct) == 'right':
                j += 1
                curdirec = [0, 1]
        day += 1
    return cnt

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dct = {}

    maxresult = 0
    for start_i in range(N):
        for start_j in range(N):
            if arr[start_i][start_j] == 0:
                sp = [start_i, start_j]
                for dr in direction:
                    for i in range(N):
                        for j in range(N):
                            dct[(i, j)] = 0

                    temparr = deepcopy(arr)
                    # print(sp, dr)
                    # print(robot(N, M, sp, dct, direction, dr, temparr))
                    maxresult = max(maxresult, robot(N, M, sp, dct, direction, dr, temparr))




    print(f'#{tc} {maxresult}')




