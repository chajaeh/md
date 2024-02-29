from collections import deque
N, T = map(int, input().split())
lst = list(map(int, input().split()))
minval = 50000000
q = deque()
for i in lst:
    q.append(i)
start = max(lst)
end = sum(lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    total = 1
    for j in range(N):
        cnt += lst[j]
        if cnt > mid:
            total += 1
            cnt = lst[j]
    if total > T:
        start = mid + 1
    elif total < T:
        end = mid - 1
    elif total == T:
        end -= 2
minval = min(minval, start)
for _ in range(N -1):
    q.rotate(1)
    start = max(lst)
    end = sum(lst)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        total = 1
        for j in range(N):
            cnt += q[j]
            if cnt > mid:
                total += 1
                cnt = q[j]
        if total > T:
            start = mid + 1
        elif total < T:
            end = mid - 1
        elif total == T:
            end -= 2
    minval = min(minval, start)
print(minval)