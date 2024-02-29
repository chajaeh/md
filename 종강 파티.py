N, M = map(int, input().split())
costlist = []
for i in range(M):
    cost6, cost1 = map(int, input().split())
    costlist.append(tuple((cost6, cost1)))
mincost6 = 1001
mincost1 = 1001
for cost6, cost1 in costlist:
    mincost6 = min(mincost6, cost6)
    mincost1 = min(mincost1, cost1)
answerlist = []
a = N * mincost1
answerlist.append(a)
b = (N // 6 +1) * mincost6
answerlist.append(b)
c = (N // 6) * mincost6 + (N % 6) * mincost1
answerlist.append(c)

print(min(answerlist))