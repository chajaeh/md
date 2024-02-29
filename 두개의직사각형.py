T = int(input())
for tc in range(1, T+1):
    x11, y11, x12, y12 = map(int, input().split())
    x21, y21, x22, y22 = map(int, input().split())
    if (x11 < x21 < x12 and y11 < y21 < y12) or (x11 < x22 < x12 and y11 < y22 < y12) or (x11 < x21 < x12 and y11 < y22 < y12) or (x11 < x22 < x12 and y11 < y21 < y12) or(x21 < x11 and y21 < y11 and x22 > x12 and y22 > y12) or (x21 > x11 and y21 > y11 and x22 < x12 and y22 < y12):
        print(f'#{tc} 1')
    elif (x12 == x21 and y11 < y21 < y12) or (x22 == x11 and y21 < y11 < y22) or (y12 == y21 and x11 < x21 < x12) or (y22 == y11 and x21 < x11 < x22):
        print(f'#{tc} 2')
    elif (x11, y11) == (x22, y22) or (x12, y11) == (x21, y22) or (x11, y12) == (x22, y21) or (x12, y12) == (x21, y21):
        print(f'#{tc} 3')
    else:
        print(f'#{tc} 4')


