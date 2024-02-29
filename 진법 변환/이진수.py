T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    a = int(a)
    num = 0
    for i in range(1, a+1):
        c = 0
        if b[i-1] == 'A':
            c = 10
        elif b[i-1] == 'B':
            c = 11
        elif b[i-1] == 'C':
            c = 12
        elif b[i-1] == 'D':
            c = 13
        elif b[i-1] == 'E':
            c = 14
        elif b[i-1] == 'F':
            c = 15
        elif b[i-1] == 'G':
            c = 16
        else:
            num += int(b[i-1]) * 16 ** (a-i)
        num += c * 16 ** (a - i)
    d = format(num, 'b')
    while len(d) < 4*a:
        d = '0' + d
    print(f'#{tc} {d}')
