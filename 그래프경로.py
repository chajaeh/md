def dfs(S, G, arr, st, visited):
    st.append(S)
    visited[S-1] = 1
    if S == G:
        return 1
    for (a, b) in arr:
        if a == S and visited[b-1] == 0:
            if dfs(b, G, arr, st, visited) == 1:
                return 1
    st.pop()
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = []
    for i in range(E):
        start, end = map(int, input().split())
        arr.append(tuple((start, end)))
    S, G = map(int, input().split())
    visited = [0] * V
    print(f'#{tc} {dfs(S, G, arr, [], visited)}')
