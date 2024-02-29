# # 어디에 단어가
# # T = int(input())
# # for tc in range(1, T+1):
# #     N, K = map(int, input().split())
# #     arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
# #     N += 1
# #     ans = 0
# #     for i in range(N):
# #         cnt = 0
# #         for j in range(N):
# #             if arr[i][j] == 0:
# #                 cnt += 1
# #             else:
# #                 if cnt == K:
# #                     ans += 1
# #                 cnt = 0
# #     for j in range(N):
# #         cnt = 0
# #         for i in range(N):
# #             if arr[i][j] == 0:
# #                 cnt += 1
# #             else:
# #                 if cnt == K:
# #                     ans += 1
# #                 cnt = 0
# #     print(f'#{tc} {ans}')
#
# #풍선팡
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     direction = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
#     result = []
#     for i in range(N):
#         for j in range(M):
#             cnt = 0
#             for dx, dy in direction:
#                 nx = j + dx
#                 ny = i + dy
#                 if 0 <= nx < M and 0 <= ny < N:
#                     cnt += arr[ny][nx]
#                 result.append(cnt)
#     print(f'#{tc} {max(result)}')
#


