cnt = 0
def func(n):
    global cnt
    if n == 1:
        return
    elif n % 2 == 0:
        cnt += 1
        return func(n/2)
    elif n % 2 == 1:
        cnt += 1
        return func(n * 3 + 1)
T = int(input())
func(T)
print(cnt)

