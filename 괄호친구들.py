mystr = str(input())
i = 0
num = 0
while i < len(mystr):
    if mystr[i] == '[':
        p1 = i
    if mystr[i] == ']':
        p2 = i
        num += int(mystr[p1+1:p2])
    if mystr[i] == '{':
        m1 = i
    if mystr[i] == '}':
        m2 = i
        num *= int(mystr[m1+1:m2])
    i += 1
print(num)
