import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dic = {} # 현재 상태를 저장할 dict
    for i in range(N): # 초기상태 (t=0 일때 key를 좌표, val를 (생명력, 번식한 시간)으로 저장)
        for j in range(M):
            if lst[i][j] != 0:
                dic[(i, j)] = (lst[i][j], 0)
    tempdic = {} # 1시간 후를 저장할 dict
    t = 0
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while t <= K:
        for (y, x), (val, time) in dic.items():
            if time + 1 + val == t: # 번식 할 수 있는 조건
                for (dy, dx) in direction:
                    if (y + dy, x + dx) not in tempdic:
                        tempdic[(y + dy, x + dx)] = (val, t)
                    else:
                        (currentval, currt) = tempdic[(y + dy, x + dx)] # 순회중 tempdict에 좌표가 이미 존재할 경우 생명력이 더 큰쪽으로 업데이트
                        maxval = max(val, currentval)
                        tempdic[(y + dy, x + dx)] = (maxval, t)
        for (y, x), (val, time) in tempdic.items():
            if (y, x) not in dic: # tempdict를 dict에 update
                dic[(y, x)] = (val, time)
        tempdic = {}
        t += 1
    cnt = 0
    for (y, x), (val, time) in dic.items():
        if 2 * val + time > K: # K 시간에 세포가 살아있을 조건
            cnt += 1
    print(cnt)