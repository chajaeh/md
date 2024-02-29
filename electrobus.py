T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    charger.append(N)
    currentpoint = 0
    count = 0
    for i in range(M+1):
        if currentpoint == N:
            break

        if currentpoint + K < charger[i]:
            count = 1
            break

        for j in range(K, 0, -1):
            if currentpoint + j in charger:
                currentpoint += j
                count += 1
                break

            else:
                continue

    print(f'#{case} {count -1}')


