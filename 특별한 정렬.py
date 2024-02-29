def specialsort(lst, N):
    sortedlist = []
    lst.sort()
    for i in range(10):
        if i % 2 == 0:
            sortedlist.append(max(lst))
            lst.remove(max(lst))
        else :
            sortedlist.append(min(lst))
            lst.remove(min(lst))
    return sortedlist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numlst = list(map(int, input().split()))
    result = specialsort(numlst, N)
    print(f'#{tc}', *result)

