sumlst = []
def func(arr, N, sum, st):
    if len(st) == N:
        sumlst.append(sum)
    for i in range(N):
        if i not in st:
            sum += arr[0][i]
            st.append(i)
            func(arr[1:], N, sum, st)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    func(arr, N, 0, [])
    print(f'#{tc} {min(sumlst)}')
    sumlst = []