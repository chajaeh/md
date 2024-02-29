def trak(N, arr, y, x, st):
    st.append((y, x))
    if (y, x) == (N-1, N-1):
        return 1
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in direction:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 0 and (ny, nx) not in st:
            if trak(N, arr, ny, nx, st):
                return 1
    return 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
st = []
print(trak(N, arr, 0, 0, st))
