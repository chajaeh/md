T = int(input())
for case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    cardsdict = {}
    for card in cards:
        if cardsdict.get(card) == None:
            cardsdict[card] = 1
        else:
            cardsdict[card] += 1

    values = [value for value in cardsdict]
    maxvalue = max(values)
    mycard = [key for key, value in cardsdict.items() if value == maxvalue]
    maxcard = max(mycard)
    print(f'#{case} {maxcard} {maxvalue}')
