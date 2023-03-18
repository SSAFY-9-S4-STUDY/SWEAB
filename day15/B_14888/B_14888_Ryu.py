import sys
input = sys.stdin.readline

num = int(input())
lst = list(map(int, input().split()))
yoensan = list(map(int, input().split()))

selection = []
for i in range(4):
    selection += [i] * yoensan[i]

# 그냥 itertools의 permutation 쓰세요 제발

the_num = 1
for i in range(1, len(selection) + 1):
    the_num *= i

max_num = -1000000000
min_num = 1000000000
for i in range(the_num):
    holly = [0] * len(selection)
    for j in range(1, len(selection) + 1):
        holly[j - 1] = i % j
        i //= j

    temp = selection[:]
    order = []
    for i in holly[::-1]:
        order.append(temp.pop(i))

    rlt = lst[0]
    for i in range(num - 1):
        if order[i] == 0:
            rlt += lst[i + 1]
        elif order[i] == 1:
            rlt -= lst[i + 1]
        elif order[i] == 2:
            rlt *= lst[i + 1]
        elif order[i] == 3:
            if rlt < 0:
                rlt = ((-1 * rlt) // lst[i + 1]) * -1
            else:
                rlt //= lst[i + 1]

    if rlt > max_num:
        max_num = rlt
    if rlt < min_num:
        min_num = rlt

print(max_num)
print(min_num)

# pypy로 2400ms 나옵니다.