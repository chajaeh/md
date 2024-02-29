T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split())) + [-1]
    i = 0
    j = 0
    while j <= N-1:
        if passcode[i] == sample[j]:
            i += 1
        else:
            j += 1
    if i == K:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')