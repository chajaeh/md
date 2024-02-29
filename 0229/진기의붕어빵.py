T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    can = "Possible"
    for i in range(N):
        boongeo = lst[i] // M * K
        if boongeo - i < 1:
            can = "Impossible"
            break
    print(f'#{tc} {can}')