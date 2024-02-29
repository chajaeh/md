T = int(input())
for tc in range(1, T+1):
    N = int(input())
    buslist = []
    for i in range(N):
        Ai, Bi = map(int, input().split())
        buslist.append(tuple((Ai, Bi)))
    P = int(input())
    stationlist = []
    mylist = [0] * 5000
    for j in range(P):
        Cj = int(input())
        stationlist.append(Cj -1)
    for start, end in buslist:
        for k in range(start, end+1):
            mylist[k] += 1
    resultlist = []
    for l in stationlist:
        resultlist.append(mylist[l])
    print(f'#{tc}', *resultlist)

