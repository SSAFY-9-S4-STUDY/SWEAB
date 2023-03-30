# lst = input().split('-')
#
# for i in range(len(lst)):
#     if '+' in lst[i]:
#         lst[i] = int(eval(lst[i]))
#     else:
#         lst[i] = int(lst[i])
#
# if len(lst) == 1:
#     print(lst[0])
# else:
#     result = lst.pop(0)
#     for num in lst:
#         result -= num
#     print(result)
# # 반례 : 03+03


lst = input().split('-')

for i in range(len(lst)):
    if '+' in lst[i]:
        temp = 0
        temp_lst = lst[i].split('+')
        for j in temp_lst:
            temp += int(j)
        lst[i] = temp
    else:
        lst[i] = int(lst[i])

result = lst.pop(0)
for i in lst:
    result -= i

print(result)