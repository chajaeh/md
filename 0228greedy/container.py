T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    weight.sort(reverse=True)
    cnt = 0
    for i in truck:
        for j in weight:
            if i >= j:
                cnt += j
                weight.remove(j)
                break
    print(f'#{tc} {cnt}')