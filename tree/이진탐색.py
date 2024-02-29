T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    cur = 1
    i = 1
    while i <= N:
        if lst[cur]:
            if cur*2+1 <= N and not lst[cur*2 +1]:
                cur = cur * 2 +1
                continue
            else:
                cur //= 2
                continue
        elif not lst[cur]:
            if cur * 2 > N or lst[cur*2]:
                lst[cur] = i
                i += 1
                continue
            else:
                cur *= 2
                continue
    print(f'#{tc} {lst[1]} {lst[N//2]}')
