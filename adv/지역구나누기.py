minnum = float("inf")
# import sys
# sys.stdin = open('input.txt', 'r')
def check(arr, Pi, N, vt, num):
    lst = [x for x in range(N)]
    for s in vt:
        lst.remove(s)
    if len(lst) == 0:
        return 1
    elif check2(arr, Pi, N, [lst[0]], num, lst):
        return 1

def check2(arr, Pi, N, vt, num, lst):
    if len(vt) == num:
        return 1
    for i in range(N):
        for j in range(len(vt)):
            if arr[vt[j]][i] == 1 and i not in vt and i in lst:
                if check2(arr, Pi, N, vt + [i], num, lst):
                    return 1

def dfs(arr, Pi, N, vt):
    global minnum
    summ = 0
    for s in vt:
        summ += Pi[s]
    if check(arr, Pi, N, vt, N - len(vt)):
        a = abs(sum(Pi) - 2 * summ)
        minnum = min(minnum, a)
    for i in range(N):
        if i not in vt and arr[i][vt[-1]]:
            dfs(arr, Pi, N, vt + [i])




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Pi = list(map(int, input().split()))
    for i in range(N):
        dfs(arr, Pi, N, [i])
    print(f'#{tc} {minnum}')
    minnum = float('inf')