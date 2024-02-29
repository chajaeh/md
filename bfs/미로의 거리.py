from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                spy, spx = i, j
                arr[i][j] = 0
            if arr[i][j] == 3:
                epy, epx = i, j
                arr[i][j] = 0
    vt = [(spy, spx)]
    q = deque()
    q.append((spy, spx))
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        (cuy, cux) = q.popleft()
        for dy, dx in di:
            ny, nx = cuy + dy, cux + dx
            if (ny, nx) not in vt and 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 0:
                q.append((ny, nx))
                arr[ny][nx] = arr[cuy][cux] + 1
    if arr[epy][epx] == 0:
        arr[epy][epx] = 1
    print(f'#{tc} {arr[epy][epx] - 1}')


