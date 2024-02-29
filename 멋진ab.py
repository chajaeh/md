cnt = 0
def ab(string):
    global cnt
    mylst = []
    for str in string:
        if len(mylst) == 0:
            mylst.append(str)
        else:
            if mylst[-1] != str:
                mylst.append(str)
            else:
                mylst.pop()
    if len(mylst) == 0:
        cnt += 1
T = int(input())
lst = []
for tc in range(T):
    a = str(input())
    lst.append(a)
for str in lst:
    ab(str)
print(cnt)

