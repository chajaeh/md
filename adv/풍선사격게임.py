scorelst = []

def shootingbaloons(lst, score):
    for i in range(len(lst)):
        if len(lst) >= 3:
            if i == 0:
                shootingbaloons(lst[1:], score + lst[i+1])
            elif i == len(lst) - 1:
                shootingbaloons(lst[:i], score+lst[i-1])
            elif 0 < i < len(lst) -1:
                shootingbaloons(lst[:i]+lst[i+1:], score + lst[i-1]*lst[i+1])
        elif len(lst) == 2:
            if i == 0:
                shootingbaloons(lst[1:2], score+lst[i-1])
            elif i == 1:
                shootingbaloons(lst[0:1], score + lst[i-1])
        elif len(lst) == 1:
            score += lst[0]
            scorelst.append(score)
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    baloons = list(map(int, input().split()))
    shootingbaloons(baloons, 0)
    print(f'#{tc} {max(scorelst)}')
    scorelst = []




