N = int(input())
reservationlist = []
for i in range(N):
    a, b = map(int, input().split())
    reservationlist.append(tuple((a, b-1)))
for start, end in reservationlist:
    meeting = [0] * 100000000

    resultlist= []
    for j in range(start, end+1):
        meeting[j] += 1
        cnt = 0
        for start2, end2 in reservationlist:
            for k in range(start2, end2):
                if meeting[k] == 1:
                    for l in range(start2, k):
                        meeting[l] == 0
                    break
                if meeting[k] == 0:
                    meeting[k] += 1
                if k == end2 -1:
                    meeting[k] = 1
                    cnt += 1
            resultlist.append(cnt)
print(max(resultlist))
