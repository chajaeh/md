T = int(input())
for tc in range(1, T+1):
    mystr = list(map(str, input().split()))
    st = []
    for strs in mystr:
        if strs in '+-*/' and len(st) <= 1:
            print(f'#{tc} error')
            break
        elif strs == '+':
            a = st.pop()
            b = st.pop()
            st.append(a+b)
        elif strs == '-':
            a = st.pop()
            b = st.pop()
            st.append(b-a)
        elif strs == '*':
            a = st.pop()
            b = st.pop()
            st.append(a*b)
        elif strs == '/':
            a = st.pop()
            b = st.pop()
            st.append(b/a)
        elif strs == '.':
            print(f'#{tc} {int(st[0])}')
        else:
            strs = int(strs)
            st.append(strs)