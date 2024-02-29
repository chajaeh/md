N, K = map(int, input().split())
chouruslist = []
for i in range(N):
    a = int(input())
    chouruslist.append(a)
maxlength = max(chouruslist)
resultlist = []
for j in range(1, maxlength + 1):
    cnt = 0
    for chourus in chouruslist:
        for k in range(K):
            if chourus - j >= 0:
                chourus = chourus -j
                cnt += 1
            if cnt == K:
                resultlist.append(j)
                break
print(max(resultlist))