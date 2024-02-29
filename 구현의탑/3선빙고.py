bingo = [list(map(int, input().split())) for _ in range(5)]
kall = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        a = kall[i][j]
        cnt = 0
        for k in range(5):
            for l in range(5):
                if bingo[k][l] == a:
                    bingo[k][l] = 0
        for k in range(5):
            if all(bingo[k][b] == 0 for b in range(5)):
                cnt += 1
            if all(bingo[b][k] == 0 for b in range(5)):
                cnt += 1
        if all(bingo[b][b] == 0 for b in range(5)):
            cnt += 1
        if all(bingo[b][4-b] == 0 for b in range(5)):
            cnt += 1
        if cnt == 3:
            print(a)
            break