T = str(input())
def func(n):
    if int(n) == 0:
        return 0
    else:
        return func(str(int(n) // 10)) + int(n[-1])

print(func(T))
