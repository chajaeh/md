result = 0
path = []
def card(cnt):
    global result
    if cnt == 4:
        result += 1
        return
    for i in lst:
        if len(path) > 0:
            if abs(path[-1] - i) <= 3:
                path.append(i)
                card(cnt + 1)
                path.pop()
        else:
            path.append(i)
            card(cnt + 1)
            path.pop()


lst = list(map(int, input()))
card(0)

print(result)