n, m = map(int,input().split())
num_list = list(map(int, input().split()))

rst = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_num = num_list[i] + num_list[j] + num_list[k]
            if sum_num > m:
                continue
            if sum_num > rst:
                rst = sum_num

print(rst)
                