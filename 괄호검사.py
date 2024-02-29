def func(string):
    lst = []
    for str in string:
        N = len(lst)
        if str == '[' or str == '{' or str == '(':
            lst.append(str)
        if str == ']' and N != 0:
            if lst[-1] != '[':
                break
            lst.pop()
        if str == '}' and N != 0:
            if lst[-1] != '{':
                break
            lst.pop()
        if str == ')' and N != 0:
            if lst[-1] != '(':
                break
            lst.pop()
        if (str == ')' or str == '}' or str == ']') and N == 0:
            lst.append(0)
            break
    if len(lst) != 0:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    mystr = str(input())
    print(f'#{tc} {func(mystr)}')

