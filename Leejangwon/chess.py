case = str(input())

clist = list(map(int, case.split()))

basic = [1, 1, 2, 2, 2, 8]

ans = [0, 0, 0, 0, 0, 0]

for i in range(6):
    ans[i] = basic[i] - clist[i]

print(ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])