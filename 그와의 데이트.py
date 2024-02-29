Y, M, D = map(str, input().split('.'))
mcnt = 1
dcnt = 1
if M == '1X':
    mcnt = 3
if M == 'X':
    mcnt = 9
if M == 'XX':
    mcnt = 3
if D == 'X':
    dcnt = 9
if D == '1X' or D == '2X':
    dcnt = 10
if D == 'XX':
    dcnt = 22
if D == '3X':
    dcnt = 2
if D == 'X0' or D == 'X1':
    dcnt = 3
if D == 'X2' or D == 'X3' or D == 'X4' or D == 'X5' or D == 'X6' or D == 'X7' or D == 'X8' or D == 'X9':
    dcnt = 2
print(mcnt * dcnt)