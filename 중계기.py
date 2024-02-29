import math
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]
    house = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                house.append(tuple((j, i)))
            if arr[i][j] == 2:
                x, y = j, i

    distance = []
    for k, l in house:
        distance.append(math.sqrt((k-x)**2 + (l-y)**2))
    print(f'#{tc} {math.ceil(max(distance))}')