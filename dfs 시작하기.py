N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
st = []
lst = []
def dfs(node, arr, N):
    visited[node] = 1
    st.append(node)
    lst.append(node)
    for i in range(N):
        if visited[i] == 0 and arr[node][i] == 1:
            dfs(i, arr, N)
    st.pop()

dfs(0, arr, N)
print(*lst)