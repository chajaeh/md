import sys
result = []
temparr = []
def func(vt, level):
    global result
    global temparr
    if level == M:
        sum = 0
        for i in range(L):
            minval = float('inf')
            for j in range(K):
                minval = min(minval, temparr[j][i])
                sum += minval
        result.append(sum)
        return
    mylst = []
    for i in range(K):
        if i not in vt:
            for j in range(L):
                mylst.append(distancelst[j][i])
            temparr.append(mylst)
            print(temparr)
            func(vt + [i], level + 1)
            temparr.pop(-1)



input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
homelst = []
chickenlst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homelst.append((i, j))
        if arr[i][j] == 2:
            chickenlst.append((i, j))
K = len(chickenlst)
L = len(homelst)
distancelst = [[] for _ in range(L)]

for i in range(K):
    (y, x) = chickenlst[i]
    sum = 0
    for j in range(L):
        (y2, x2) = homelst[j]
        distancelst[j].append(abs(y2 - y) + abs(x2 - x))
func([], 0)
print(distancelst)
print(min(result))

