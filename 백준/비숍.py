import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
result = []


def dfs(N, arr, cnt, vt):
    a = 0
    tempvt = deepcopy(vt)
    global result
    changed = False
    for (i, j) in bishoplst:
        if (i, j) not in vt:
            changed = True
            for (k, l) in bishoplst:
                if abs(k - i) == abs(j - l):
                    tempvt.append((k, l))
                    a += 1
            dfs(N, arr, cnt + 1, tempvt)
            tempvt.pop()

    if not changed:
        result.append(cnt)

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bishoplst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bishoplst.append((i, j))
dfs(N, arr, 0, [])
print(max(result))