T = int(input())
for tc in range(1, T+1):
    N = int(input())
    station = list(map(int, input().split()))
    answerlist = [0]

    for station1 in range(N):
        if station1 + 2 < N:
            for station2 in range(station1 + 2, N):
                for station3 in range(N):
                    if station3 + 2 < N:
                        for station4 in range(station3 + 2, N):
                            if abs(station1 - station2) >= 2 and abs(station3 - station4) >= 2 and abs(station1 - station3) >= 2 and abs(station1 - station4) >= 2 and abs(station2 - station3) >= 2 and abs(station2 - station4) >= 2:
                                if (station1 == 0 and station4 == N-1) or (station3 == 0 and station2 == N-1) or (station1 == 0 and station2 == N-1) or (station3 == 0 and station4 == N-1):
                                    pass
                                elif station1 < station3 < station2 and station1 < station4 < station2:
                                        answerlist.append((station[station1] + station[station2])**2 + (station[station3] + station[station4])**2)
                                elif (station3 < station1 or station3 > station2) and (station4 < station1 or station4 > station2):
                                    answerlist.append((station[station1] + station[station2]) ** 2 + (
                                                    station[station3] + station[station4]) ** 2)


    print(f'#{tc} {max(answerlist)}')