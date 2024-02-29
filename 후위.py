string = str(input())
st = []
val = 0
for strs in string:
    if strs == '+':
        a = st.pop()
        a = int(a)
        b = st.pop()
        b = int(b)
        st.append(a+b)
    elif strs == '-':
        a = st.pop()
        a = int(a)
        b = st.pop()
        b = int(b)
        st.append(b-a)
    else:
        st.append(strs)
print(*st)
