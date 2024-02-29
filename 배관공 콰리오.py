N, L = map(int, input().split())
pipelist = list(map(int, input().split()))
pipelist.sort()

for pipe in pipelist:
    for i in range(1, L):
        if pipe + i in pipelist:
            pipelist.remove(pipe + i)
print(len(pipelist))