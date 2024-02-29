# def tour(lst, N, dict):
#     if N > 2 and N % 2 == 1:
#         c = tour(lst[:N//2], N//2, dict)
#         d = tour(lst[N//2:], N//2 + 1, dict)
#         return rsp(c, d, dict)
#
#     elif N > 2 and N % 2 == 0:
#         c = tour(lst[:N//2], N//2, dict)
#         d = tour(lst[N//2:], N//2, dict)
#         return rsp(c, d, dict)
#
#     elif N == 2:
#         a = lst[0]
#         b = lst[1]
#         return rsp(a, b, dict)
#
#     elif N == 1:
#         return lst[0]
#
# def rsp(a, b, dict):
#     if dict[a] == 1 and dict[b] == 2:
#         return b
#     elif dict[a] == 1 and dict[b] == 3:
#         return a
#     elif dict[a] == 2 and dict[b] == 1:
#         return a
#     elif dict[a] == 2 and dict[b] == 3:
#         return b
#     elif dict[a] == 3 and dict[b] == 1:
#         return b
#     elif dict[a] == 3 and dict[b] == 2:
#         return a
#     elif dict[a] == dict[b]:
#         return min(a, b)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     dict = {}
#     for i in range(N):
#         dict[i+1] = lst[i]
#     mylst = []
#     for i in range(1, N+1):
#         mylst.append(i)
#     print(f'#{tc} {tour(mylst, N, dict)}')


def TNT(start, end):
    if start == end:
        return start #부전승
    a = TNT(start, (start + end) // 2) #짝수번째
    b = TNT((start + end) // 2 +1, end)#홀수번쨰
    return RSP(a,b)
def RSP(x,y):
    if cards[x] == cards[y]:
        return x
    elif cards[x] - cards[y] == 1 or cards[x] - cards[y] == -2:
        return x
    else:
        return y
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = TNT(0, N-1) +1
    print(f'#{tc} {result}')