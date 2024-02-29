def binarySearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result_A = binarySearch(P, A)
    result_B = binarySearch(P, B)

    if result_A < result_B:
        print(f'#{tc} A')
    elif result_A > result_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
