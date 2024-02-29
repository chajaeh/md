from collections import deque
from copy import deepcopy
def bfs(N, arr):
    arr2 = [[0, 0]] + arr
    q = deque()
    time = [0] * (N+1) # time[i] = i번째 task까지 처리했을 경우 걸리는 총 시간
    time[0] = 1
    adjl = [[] for _ in range(N+1)] # adjl[i] 에 i번 task를 처리할 시 할 수 있는 다음 task의 번호들이 들어간다
    adjl2 = [[] for _ in range(N+1)]# adjl2[i]에 i번 task의 선행 과제들의 번호가 들어간다
    for i in range(1, N+1):
        if len(arr2[i]) == 2: # 선행과제가 없을 경우 가장 먼저 deque에 들어간다
            q.append(i)
            time[i] = arr2[i][0]
        else:
            for j in range(2, len(arr2[i])):
                adjl[arr2[i][j]].append(i)
                adjl2[i].append(arr2[i][j])
    if len(q) == 0: # 선행과제가 없는 task가 하나도 없을 경우 return
        return -1
    while q:
        a = q.popleft()
        if len(adjl[a]) != 0:
            for i in adjl[a]:
                adjl2[i].remove(a)
                time[i] = max(time[i], time[a] + arr2[i][0])
                if time[i] > minval:
                    return -1
                if len(adjl2[i]) == 0:
                    q.append(i)
    check = False
    for sublst in adjl2:
        if len(sublst) != 0:
            check = True
    if check == True:
        return -1
    else:
        return max(time)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minval = 500001
    for i in range(N):
        temparr = deepcopy(arr)
        temparr[i][0] //= 2
        a = bfs(N, temparr)
        if a != -1:
            minval = min(minval, a)
    if minval != 500001:
        print(f'#{tc} {minval}')
    else:
        print(f'#{tc} -1')