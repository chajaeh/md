T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answerlist = list(map(int, input().split()))
    studentlist = [list(map(int, input().split())) for _ in range(N)]
    scorelist = []

    for i in range(N):
        scoresum = 0
        score = 0
        for j in range(M):
            if studentlist[i][j] == answerlist[j]:
                score += 1
                scoresum += score
            else:
                score = 0
        scorelist.append(scoresum)

    print(f'#{tc} {max(scorelist) - min(scorelist)}')
