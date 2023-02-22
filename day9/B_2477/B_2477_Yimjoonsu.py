# per_sqm = int(input())
#
# length = []
# x = []
# y = []
#
# for i in range(6):
#     a, b = map(int, input().split())
#     length.append(b)
#     if a == 1 or a == 2:
#         x.append(b)
#     else:
#         y.append(b)
#
# whole_area = max(x) * max(y)
# del length[length.index(max(x))]
# del length[length.index(max(y))]
# print((whole_area - length[1] * length[2]) * per_sqm)
# 런타임 에러


per_sqm = int(input())

lst = []
x = []
y = []
no_melon = []

for i in range(6):
    card, length = map(int, input().split())
    lst.append([card, length])
    if card == 1 or card == 2:
        x.append(length)
    else:
        y.append(length)
whole_area = max(x) * max(y)

for i in range(6):
    if lst[i][0] == lst[(i+2)%6][0]:
        no_melon.append(lst[(i+1)%6][1])

print((whole_area - no_melon[0] * no_melon[1]) * per_sqm)

# 비슷하게 접근한 것 찾아서 참고했습니다