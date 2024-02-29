cnt = 0
def func(n):
    global cnt
    if n <= 0:
        return 0
    if n == 20:
        return 3
    if n == 10:
        return 1
    else:
        return func(n-10)  + func(n-20) * 2



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc} {func(n)}')