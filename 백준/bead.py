import sys
result = 11

def left(red, blue, level, st):
    [ry, rx] = red
    [by, bx] = blue
    for i in range(0, M):
        if [ry, rx -i] == O:
            rx -= i
            break
        elif [ry, rx - i] == [by, bx] or [ry, rx - i] in lstob:
            rx -= (i - 1)
            break
    for i in range(0, M):
        if [by, bx - i] == O:
            bx -= i
            break
        elif [by, bx - i] == [ry, rx] or [by, bx - i] in lstob:
            bx -= (i - 1)
            break
    for i in range(0, M):
        if [ry, rx -i] == O:
            rx -= i
            break
        elif [ry, rx - i] == [by, bx] or [ry, rx - i] in lstob:
            rx -= (i - 1)
            break
    if [[ry, rx], [by, bx]] not in st:
        simulation([ry, rx], [by, bx], level, st + [[ry, rx], [by, bx]])




def right(red, blue, level, st):
    [ry, rx] = red
    [by, bx] = blue
    for i in range(0, M):
        if [ry, rx + i] == O:
            rx += i
            break
        elif [ry, rx + i] == [by, bx] or [ry, rx + i] in lstob:
            rx += (i - 1)
            break
    for i in range(0, M):
        if [by, bx + i] == O:
            bx += i
            break
        elif [by, bx + i] == [ry, rx] or [by, bx + i] in lstob:
            bx += (i - 1)
            break
    for i in range(0, M):
        if [ry, rx + i] == O:
            rx += i
            break
        elif [ry, rx + i] == [by, bx] or [ry, rx + i] in lstob:
            rx += (i - 1)
            break
    if [[ry, rx], [by, bx]] not in st:
        simulation([ry, rx], [by, bx], level, st + [[ry, rx], [by, bx]])


def up(red, blue, level, st):
    [ry, rx] = red
    [by, bx] = blue
    for i in range(0, N):
        if [ry - i, rx] == O:
            ry -= i
            break
        elif [ry - i, rx] == [by, bx] or [ry - i, rx] in lstob:
            ry -= (i - 1)
            break
    for i in range(0, N):
        if [by - i, bx] == O:
            by -= i
            break
        elif [by - i, bx] == [ry, rx] or [by - i, bx] in lstob:
            by -= (i - 1)
            break
    for i in range(0, N):
        if [ry - i, rx] == O:
            ry -= i
            break
        elif [ry - i, rx] == [by, bx] or [ry - i, rx] in lstob:
            ry -= (i - 1)
            break
    if [[ry, rx], [by, bx]] not in st:
        simulation([ry, rx], [by, bx], level, st + [[ry, rx], [by, bx]])

def down(red, blue, level, st):
    [ry, rx] = red
    [by, bx] = blue
    for i in range(0, N):
        if [ry + i, rx] == O:
            ry += i
            break
        elif [ry + i, rx] == [by, bx] or [ry + i, rx] in lstob:
            ry += (i - 1)
            break
    for i in range(0, N):
        if [by + i, bx] == O:
            by += i
            break
        elif [by + i, bx] == [ry, rx] or [by + i, bx] in lstob:
            by += (i - 1)
            break
    for i in range(0, N):
        if [ry + i, rx] == O:
            ry += i
            break
        elif [ry + i, rx] == [by, bx] or [ry + i, rx] in lstob:
            ry += (i - 1)
            break
    if [[ry, rx], [by, bx]] not in st:
        simulation([ry, rx], [by, bx], level, st + [[ry, rx], [by, bx]])

direction = [(1,0), (0,1), (0,-1), (-1,0)]

def simulation(red, blue, level, st):
    global result
    [ry, rx] = red
    [by, bx] = blue
    if [ry, rx] == O and [by, bx] != O:
        result = min(result, level)
        return
    if level >= result:
        return


    elif [by, bx] == O:
        return

    for dy, dx in direction:
        rny = ry + dy
        rnx = rx + dx
        bny = by + dy
        bnx = bx + dx
        if [dy, dx] == [0, 1]:
            if ([rny, rnx] in lstob and [bny, bnx] == [ry, rx]) or ([bny, bnx] in lstob and [rny, rnx] == [by, bx]):
                pass
            else:
                right(red, blue, level + 1, st)
        if [dy, dx] == [0, -1]:
            if ([rny, rnx] in lstob and [bny, bnx] == [ry, rx]) or ([bny, bnx] in lstob and [rny, rnx] == [by, bx]):
                pass
            else:
                left(red, blue, level + 1, st)
        if [dy, dx] == [1, 0]:
            if ([rny, rnx] in lstob and [bny, bnx] == [ry, rx]) or ([bny, bnx] in lstob and [rny, rnx] == [by, bx]):
                pass
            else:
                down(red, blue, level + 1, st)
        if [dy, dx] == [-1, 0]:
            if ([rny, rnx] in lstob and [bny, bnx] == [ry, rx]) or ([bny, bnx] in lstob and [rny, rnx] == [by, bx]):
                pass
            else:
                up(red, blue, level + 1, st)


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
lstob = []
lstdot = []

for i in range(N):
    for j in range(M):
        a = arr[i][j]
        if a == "#":
            lstob.append([i, j])
        if a == "R":
            R = [i, j]
        if a == "B":
            B = [i, j]
        if a == "O":
            O = [i, j]
        if a == ".":
            lstdot.append([i, j])
simulation(R, B, 0, [R, B])
if result <= 10:
    print(result)
else:
    print(-1)