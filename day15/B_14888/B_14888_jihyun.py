# dfs로 풀라고 힌트 주신 재현아! 고마워!
def dsf(plus, minus, multi, div, index, tmp_val):
    global maxi, mini
    if index == N:
        maxi = max(maxi, tmp_val)
        mini = min(mini, tmp_val)
        return

    if plus:
        dsf(plus - 1, minus, multi, div, index + 1, tmp_val + nums[index])
    if minus:
        dsf(plus, minus - 1, multi, div, index + 1, tmp_val - nums[index])
    if multi:
        dsf(plus, minus, multi - 1, div, index + 1, tmp_val * nums[index])
    if div:
        if tmp_val >= 0:
            next_val = tmp_val // nums[index]
        else:
            next_val = -(-tmp_val // nums[index])
        dsf(plus, minus, multi, div - 1, index + 1, next_val)


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

maxi = - 10 ** 9
mini = 10 ** 9

dsf(operators[0], operators[1], operators[2], operators[3], 1, nums[0])
print(maxi, mini)
