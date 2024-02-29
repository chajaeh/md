def comb(n, r):
    num = 1
    for i in range(r):
        num *= (n - i)
        num /= (i+1)
    return num
N, K = map(int, input().split())
num1 = (N+1) // 2
num2 = N // 2
cnt = 0
for i in range(K, 2*K+1):
    if i % 3 == 0:
        need1 = 2*K - i
        need2 = i - K
        if num1 >= need1 and num2 >= need2:
            cnt += comb(num1, need1) * comb(num2, need2)
print(int(cnt))