N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
check_lst = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_card = num_lst[i] + num_lst[j] + num_lst[k]
            if sum_card <= M:
                check_lst.append(sum_card)

print(max(check_lst))
