N = int(input())
Q = int(input())
color = [list(map(int, input().split())) for _ in range(Q)]
arr = [[0] * (N+10) for _ in range(N+10)]

for cl, y1, x1, y2, x2 in color:
    for i in range(abs(y2 - y1) + 1):
        for j in range(abs(x2 - x1) + 1):
            if arr[min(y2, y1) + i][min(x2, x1) + j] < cl:
                arr[min(y2, y1) + i][min(x2, x1) + j] = cl

result = []
for i in range(N):
    for j in range(N):
        curr = arr[i][j]
        a = 1
        while True:
            if curr != 0 and i + a < N and j + a < N and all(arr[i + b][j + a] == curr for b in range(a + 1)) and all(arr[i + a][j + b] == curr for b in range(a + 1)):
                result.append((a + 1) ** 2)
                a += 1
            else:
                break
if len(result) != 0:
    print(max(result))
else:
    print(0)
