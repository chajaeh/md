T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    lst2 = [[] for _ in range(E+2)]
    for i in range(E):
        lst2[lst[2*i]].append(lst[2*i+1])
    cnt = 1
    q = []
    q.append(N)
    while q:
        a = q.pop(0)
        for i in lst2[a]:
            q.append(i)
            cnt += 1

    print(f'#{tc} {cnt}')



