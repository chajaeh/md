def binarysearch(lst, N, key):
    start = 0
    end = N-1
    lst.sort()
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == key:
            return "O"
        elif lst[middle] < key:
            start = middle +1
        else:
            end = middle -1
    return "X"

n = int(input())
numlst = list(map(int, input().split()))
k = int(input())
findinglst = list(map(int, input().split()))

for i in findinglst:
    print(binarysearch(numlst, n, i), end="")