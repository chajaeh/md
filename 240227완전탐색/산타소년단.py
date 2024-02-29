N = int(input())
num = 1
for i in range(N):
    num *= (5 - i)
print(int(num * 3 / 5))