T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        sp = arr[i][0]
        ep = arr[i][1]
        for j in range(N):
            if i != j:
                sp2 = arr[j][0]
                ep2 = arr[j][1]
                if sp < sp2:
                    if ep < ep2:
                        pass
                    else:
                        cnt += 1
                if sp > sp2:
                    if ep > ep2:
                        pass
                    else:
                        cnt += 1
    print(f'#{tc} {int(cnt/2)}')