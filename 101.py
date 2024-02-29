def fx(lst, N, val, string):
    if len(lst) == 1 and val % 101 == 0 and val > 0:
        print(string)
        return 0
    if len(lst) == 1:
        return 0
    operator = ["*", '+', "-"]
    for op in operator:
        if op == "*":
            new_val = val * int(lst[1])
            new_string = f"{string}*{lst[1]}"
            fx(lst[1:], N, new_val, new_string)
        elif op == "+":
            new_val = val + int(lst[1])
            new_string = f"{string}+{lst[1]}"
            fx(lst[1:], N, new_val, new_string)
        elif op == "-":
            new_val = val - int(lst[1])
            new_string = f"{string}-{lst[1]}"
            fx(lst[1:], N, new_val, new_string)

N = int(input())
nums = list(map(str, input().split()))
fx(nums, N, int(nums[0]), nums[0])
