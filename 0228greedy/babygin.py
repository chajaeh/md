
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    player1 = []
    player2 = []
    i = 0
    checked = False
    for i in range(6):
        player1.append(lst[2*i])
        player2.append(lst[2*i + 1])

        if i >= 2:
            checked2 = False
            for j in range(i+1):
                if player1.count(player1[j]) >= 3 or (player1[j] + 1 in player1 and player1[j] + 2 in player1):
                    checked = True
                    checked2 = True
                    print(f'#{tc} 1')
                    break
                if player2.count(player2[j]) >= 3 or (player2[j] + 1 in player2 and player2[j] + 2 in player2):
                    checked = True
                    checked2 = True
                    print(f'#{tc} 2')
                    break
        if checked:
            break

    if not checked:
        print(f'#{tc} 0')
