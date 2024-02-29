A, B = map(int, input().split())
st = []
vt = [0] * 6
val = 0
arr = [[0, 0, 1, 0, 1, 1], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]


def search(arr, A, B):
    global val
    if A == B:
        print(val)
        return
    st.append(A)
    vt[A - 1] = 1
    found_path = False
    for i in range(6):
        if arr[A - 1][i] == 1 and vt[i] == 0:
            val += 1
            search(arr, i + 1, B)
            found_path = True
            break
    if not found_path:
        print(0)
    val -= 1
    st.pop()


search(arr, A, B)