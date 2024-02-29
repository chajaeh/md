T = int(input())
for tc in range(1, T+1):
    num = float(input())
    i = -1
    mystr = ''
    while num > 0:
        if num >= 2 ** i:
            num -= 2 ** i
            mystr = mystr + '1'
        else:
            mystr = mystr + '0'
        if i < -12:
            break
        i -= 1

    if num == 0:
        print(f'#{tc} {mystr}')
    else:
        print(f'#{tc} overflow')

