N, M = map(int, input().split())
lst = list(map(int, input().split()))
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
    if total > M:
        start = mid + 1
    elif total < M:
        end = mid - 1
    elif total == M:
        end -= 2

print(start)