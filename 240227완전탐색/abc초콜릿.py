result = 0
lst = []
def choco(cnt, used):
    global result
    if cnt == N:
        result += 1
        return
    for i in range(3):
        if used[i] == 0:
            if i == 0:
                choco(cnt + 1, [1, 0, 0])
            elif i == 1:
                choco(cnt + 1, [0, 1, 0])
            elif i == 2:
                choco(cnt + 1, [0, 0, 1])

        elif used[i] == 1:
            if i == 0:
                choco(cnt + 1, [2, 0, 0])
            elif i == 1:
                choco(cnt + 1, [0, 2, 0])
            elif i == 2:
                choco(cnt + 1, [0, 0, 2])



N = int(input())
choco(0, [0, 0, 0])
print(result)
