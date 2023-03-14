# 문제 추천하신 분을 찾습니다~ 

import sys
from collections import deque
input = sys.stdin.readline
root = int(input())
stk = deque([root])
dict = {root: [0, 0]}
while True:
    try:
        num = int(input())
        while stk and stk[-1] < num:
            if len(stk) == 1:
                dict[stk[-1]][1] = num
            elif stk[-2] > num:
                dict[stk[-1]][1] = num
            stk.pop()
        if stk and dict[stk[-1]][0] == 0:
            dict[stk[-1]][0] = num
        stk.append(num)
        dict[num] = [0, 0]
    except:
        break

stk2 = deque([root])

# 재귀함수와 stack은 본질적으로 같은 메커니즘이라는 것에 착안했습니다.

while stk2:
    temp = stk2[-1]

    if dict[temp] == [0, 0]:
        a = stk2.pop()
        print(a)
    else:
        if dict[temp][1] != 0:
            stk2.append(dict[temp][1])
            dict[temp][1] = 0

        if dict[temp][0] != 0:
            stk2.append(dict[temp][0])
            dict[temp][0] = 0










