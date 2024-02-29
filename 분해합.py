N = int(input())
sumlist = []
for i in range(1, N):
    str_i = str(i)
    strlist = list(map(str, str_i))
    sumval = i
    for j in strlist:
        k = int(j)
        sumval += k
    if sumval == N:
        sumlist.append(i)
if len(sumlist) == 0:
    print(0)
else:
    print(sumlist[0])