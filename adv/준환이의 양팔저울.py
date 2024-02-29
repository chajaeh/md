from itertools import permutations

T = int(input())
def dfs(lst, L, R, curr):
    global cnt

    if lst_sum - (L + R) + R <= L: # 현재 왼쪽에 올라가 있는 무게가 나머지 무게의 합 이상일 경우 나머지는 아무데나 올려도 상관 x
        cnt += 2 ** (N - curr)
        return 0


    if R + lst[curr] <= L: # 오른쪽에 올리기
        dfs(lst, L, R + lst[curr], curr + 1)
        dfs(lst, L + lst[curr], R, curr + 1)
    else:
        dfs(lst, L + lst[curr], R, curr + 1) # 왼쪽에 올리기


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst_sum = sum(lst)
    per = permutations(lst, N) # 원소의 개수가 N개인 permutation 생성 - 그 subset의 원소의 순서가 추를 올려놓는 순서가 된다
    cnt = 0
    for i in per: # 처음 1개 올려놓고 시작
        dfs(i, i[0], 0, 1)
    print(f'#{tc} {cnt}')
