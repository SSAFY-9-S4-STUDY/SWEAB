N = int(input())

case1 = [4, 2, 3, 1, 3, 1]  # 14
case2 = [3, 1, 4, 2, 4, 2]  # 16
case3 = [2, 3, 1, 4, 1, 4]  # 15
case4 = [1, 4, 2, 3, 2, 3]  # 15

arr_direct = []
arr_length = []

for _ in range(6):
    a, b = map(int, input().split())
    arr_direct.append(a)
    arr_length.append(b)

if sum(arr_direct) == 14:
    ans = N * ((arr_length[arr_direct.index(4)] * arr_length[arr_direct.index(2)]) - (arr_length[arr_direct.index(4) - 2] * arr_length[arr_direct.index(4) - 3]))
elif sum(arr_direct) == 16:
    ans = N * ((arr_length[arr_direct.index(3)] * arr_length[arr_direct.index(1)]) - (arr_length[arr_direct.index(3) - 2] * arr_length[arr_direct.index(3) - 3]))
else:
    if arr_direct.count(4) == 2:
        ans = N * ((arr_length[arr_direct.index(2)] * arr_length[arr_direct.index(3)]) - (arr_length[arr_direct.index(2) - 2] * arr_length[arr_direct.index(2) - 3]))
    else:
        ans = N * ((arr_length[arr_direct.index(1)] * arr_length[arr_direct.index(4)]) - (arr_length[arr_direct.index(1) - 2] * arr_length[arr_direct.index(1) - 3]))

print(ans)