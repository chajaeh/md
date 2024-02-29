# import itertools
#
#
# def dfs(arr, a, b, N, M, st, sumval):
#     sumval += arr[a][b]
#     st.append((a, b))
#
#     if len(st) == 4:
#         resultlst.append(sumval)
#     else:
#         if b % 2 == 0:
#             direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1)]
#         else:
#             direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1)]
#
#         for (dy, dx) in direction:
#             ny = a + dy
#             nx = b + dx
#             if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in st:
#                 dfs(arr, ny, nx, N, M, st, sumval)
#
#     st.pop()
#
#
# def dfs2(arr, a, b, N, M):
#
#     if b % 2 == 0:
#         direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1)]
#         subset = itertools.combinations(direction, 3)
#     else:
#         direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1)]
#         subset = itertools.combinations(direction, 3)
#
#     for i in subset:
#         sumval = arr[a][b]
#         for dy, dx in i:
#             ny = a + dy
#             nx = b + dx
#             if 0 <= ny < N and 0 <= nx < M:
#                 sumval += arr[ny][nx]
#         resultlst.append(sumval)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     resultlst = []
#
#     for i in range(N):
#         for j in range(M):
#             dfs(arr, i, j, N, M, [], 0)
#             dfs2(arr, i, j, N, M)
#
#     print(f'#{tc} {max(resultlst)}')

# 양봉업자 코코

# 양봉업자 코코
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0


    def bee(y, x, cnt, val):
        global max_val
        if 0 > y or 0 > x or y >= N or x >= M:
            return
        if cnt == 4:
            max_val = max(val + arr[y][x], max_val)
            return
        honey = arr[y][x]
        arr[y][x] = 0
        bee(y + 1, x, cnt + 1, val + honey)
        bee(y - 1, x, cnt + 1, val + honey)
        bee(y, x - 1, cnt + 1, val + honey)
        bee(y, x + 1, cnt + 1, val + honey)

        if x % 2 == 0:  # 짝수면 위 대각선도 됨
            bee(y - 1, x + 1, cnt + 1, val + honey)
            bee(y - 1, x - 1, cnt + 1, val + honey)
        else:  # 홀수면 아래 대각선도 됨
            bee(y + 1, x - 1, cnt + 1, val + honey)
            bee(y + 1, x + 1, cnt + 1, val + honey)

        arr[y][x] = honey


    dir_d = [(0, -1), (0, 1), (1, 0)]  # y, x
    dir_u = [(0, -1), (0, 1), (-1, 0)]


    def cross_T_up(y, x):  # t모양 찾기
        global max_val
        val = arr[y][x]
        for d in range(3):
            ny = dir_u[d][0] + y
            nx = dir_u[d][1] + x
            if 0 <= ny < N and 0 <= nx < M:
                val += arr[ny][nx]
            else:
                return
        max_val = max(val, max_val)


    def cross_T_down(y, x):  # t모양 찾기
        global max_val
        val = arr[y][x]
        for d in range(3):
            ny = dir_d[d][0] + y
            nx = dir_d[d][1] + x
            if 0 <= ny < N and 0 <= nx < M:
                val += arr[ny][nx]
            else:
                return
        max_val = max(val, max_val)


    for i in range(N):
        for j in range(M):
            bee(i, j, 1, 0)
            cross_T_up(i, j)
            cross_T_down(i, j)
    print(f'#{tc} {max_val}')