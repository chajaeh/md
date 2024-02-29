
T = int(input())
for tc in range(1, T+1):
    r = int(input())
    cnt = 0
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            if i**2 + j**2 <= r ** 2:
                cnt += 1
    print(f'#{tc} {cnt}')

