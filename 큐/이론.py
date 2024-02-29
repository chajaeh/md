# 스택 : 후입선출
# DFS에 이용
#
# 큐 : 선입선출
# deque #fromcollections import deque
# 선입 append() 선출 popleft()
# BFS에 활용
#
# 우선순위큐
# 우선순위로 큐가 추가, 우선순위가 높은것부터 제거
# heapq 모듈 사용, import heapq
# heappush, heappop


import heapq
q = []

heapq.heappush(q, 4)
heapq.heappush(q, 3)
heapq.heappush(q, 1)
heapq.heappush(q, 7)

ans1 = heapq.heappop(q)
ans2 = heapq.heappop(q)
print(ans1, ans2)
print(q)