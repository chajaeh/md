T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    start = 0
    end = 25
    while True:
        changed = False
        for i in lst:
            if i[0] >= start:
                if end > i[1]:
                    changed = True
                    end = i[1]
                    k = i[0]
                    continue
        if not changed:
            break
        start = end
        end = 25
        cnt += 1
    print(f'#{tc} {cnt}')