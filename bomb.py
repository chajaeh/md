N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '@':
            for k in range(1, K+1):
                for a in range(3):
                    ny, nx = i + (k*dy[a]), j + (k*dx[a])
                    if 0 <= ny < N and 0 <= nx < M:
                        if arr[ny][nx] in ('#', '@'):
                            break
                        else:
                            arr[ny][nx] = '%'
for row in arr:
    print(''.join(row))

# direction = []
#
# for i in range(1, K+1):
#     direction.append(tuple((i, 0)))
#     direction.append(tuple((-i, 0)))
#     direction.append(tuple((0, i)))
#     direction.append(tuple((0, -i)))


# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '@':
#             for k in range(1, K+1):
#                 if i+k < N and arr[i + k][j] not in ('#', '@'):
#                     arr[i + k][j] = '%'
#                 else:
#                     break
#             for k in range(1, K+1):
#                 if i-k >= 0 and arr[i - k][j] not in ('#', '@'):
#                     arr[i - k][j] = '%'
#                 else:
#                     break
#             for k in range(1, K+1):
#                 if j+k < M and arr[i][j + k] not in ('#', '@'):
#                     arr[i][j + k] = '%'
#                 else:
#                     break
#             for k in range(1, K+1):
#                 if j-k >= 0 and arr[i][j - k] not in ('#', '@'):
#                     arr[i][j - k] = '%'
#                 else:
#                     break
#             arr[i][j] = '%'
# for row in arr:
#     print(''.join(row))
