N = int(input())

group_of_ans = []
for m5 in range(N // 5 + 1):
    for m3 in range(N // 3 + 1):
        if m5 * 5 + m3 * 3 == N:
            group_of_ans.append((m5, m3))

if len(group_of_ans) == 0:
    group_of_ans.append((-1, 0))

min_value = min(group_of_ans, key = lambda x: sum(x))
print(sum(min_value))