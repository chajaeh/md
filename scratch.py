def gravity(lst):
    max_v = 0
    for i in range(L):
        count = 0
        for j in range(i + 1, L):
            if lst[i] > lst[j]:
                count += 1
        max_v = max(max_v, count)
    return max_v

T = int(input())
for case in range(1, T+1):
    L = int(input())
    boxes = list(map(int, input().split()))
    print(f'#{case} {gravity(boxes)}')


