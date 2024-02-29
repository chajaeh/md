A, B =map(int, input().split())

cnt = 0

while A < B:
    if B % 2 == 0:
        B = B / 2
        cnt += 1
    elif B - (B // 10 * 10) == 1:
        B = (B - 1) / 10
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)

