import sys
input = sys.stdin.readline

num = int(input())
lst = [list(map(int, input().split())) for _ in range(num)]

min_num = 40000


def recursion(now):
    global min_num, num, lst

    if min_num == 0:
        return

    if len(now) == num//2:
        l_lst = list(set(range(num)) - set(now))
        rlt = 0
        for i in range(num//2):
            for j in range(num//2):
                rlt += lst[now[i]][now[j]] - lst[l_lst[i]][l_lst[j]]

        if abs(rlt) < min_num:
            min_num = abs(rlt)

    for i in range(num):
        if not now or i > now[-1]:
            recursion(now + [i])

        # if i not in now:  이렇게 하면 중복을 못막아서 시간초과가 난다.

recursion([])
print(min_num)