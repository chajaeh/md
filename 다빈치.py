import copy
st = []
result = 9 ** 40
myarr = []
def dfs(arr, M, lst, i, val, vt):
    global result
    global myarr
    vt[i] = 1
    val *= arr[i]
    st.append(i)
    lst.append(arr[i])
    if len(st) > M:
        return
    if len(st) == M and result > val:
        vt[i] = 0
        result = val
        myarr = copy.deepcopy(lst)


    for i in range(len(arr)):
        if i not in st:
            dfs(arr, M, lst, i, val, vt)
    st.pop()
    lst.pop()
    vt[i] = 0

N, M = map(int, input().split())
numlst = list(map(int, input().split()))
vt = [0] * N
dfs(numlst, M, [], 0, 1, vt)
myarr.sort()
print(*myarr)