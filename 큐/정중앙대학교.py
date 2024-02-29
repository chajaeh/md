import heapq
q = []
heapq.heappush(q, 500)
N = int(input())
for i in range(N):
    score1, score2 = map(int, input().split())
    heapq.heappush(q, score1)
    heapq.heappush(q, score2)
    q.sort()
    print(q[i+1])

