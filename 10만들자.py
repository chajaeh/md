result = 0
def test(N, val, sum):
    global result
    if sum > 10:
        return
    if sum == 10 and val == N:
        result += 1
        return 0
    if val == N:
        return 0
    for i in range(1, 10):
        test(N, val+1, sum+i)


N = int(input())
test(N, 0, 0)
print(result)