def func(strs):
    while True:
        removed = False
        for i in range(1, len(strs)):
            if strs[i] == strs[i-1]:
                strs = strs[0:i-1] + strs[i+1:]
                removed = True
                break

        if not removed:
            print(f'#{tc} {len(strs)}')
            return 0

T = int(input())
for tc in range(1, T+1):
    strs = str(input())
    func(strs)
