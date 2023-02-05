N = int(input())

num_list = [list(map(int, input().split()))for _ in range(N)]

# for i in range(N - 1, 0, -1):
#     for j in range(i):
#         if num_list[j][0] > num_list[j + 1][0]:
#             num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j] 
#         elif num_list[j][0] == num_list[j + 1][0]:
#             if num_list[j][1] > num_list[j + 1][1]:
#                 num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j] 

num_list = sorted(num_list)

for num in num_list:
    print(*num)