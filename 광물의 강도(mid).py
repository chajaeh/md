def Binarysearch(lst, Si, Ei):
    cnt = 0
    for i in lst:
        if Si <= i <= Ei:
            cnt += 1
    return cnt



N, Q = map(int, input().split())
orelist = list(map(int, input().split()))

for i in range(Q):
    Si, Ei = map(int, input().split())
    print(Binarysearch(orelist, Si, Ei))
