T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    cnt = 0
    for st1 in str1:
        cnt2 = 0
        for st2 in str2:
            if st1 == st2:
                cnt2 +=1
        cnt = max(cnt, cnt2)
    print(f'#{tc} {cnt}')

