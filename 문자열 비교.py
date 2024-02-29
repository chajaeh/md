T = int(input())
for tc in range(1, T+1):
    s1 = str(input())
    s2 = str(input())
    if s1 in s2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')