### 아이디어는 있으나 구현을 어떻게 해야할지 아이디어를 떠올리지 못했습니다....
### 그에 따라 구글링을 하여 해당 코드를 공부하는 방식으로 진행했습니다.

import sys
sys.setrecursionlimit(10**5)
def post_order(start, end):
    if start > end:
        return

    root = n_lst[start]
    pivot = end + 1
    for i in range(start + 1, end + 1):
        if root < n_lst[i]:
            pivot = i
            break
    post_order(start + 1, pivot - 1)
    post_order(pivot, end)
    print(root)


n_lst = list()
while True:
    n = sys.stdin.readline().strip()
    if not n:
        break
    n_lst.append(int(n))

if n_lst:
    post_order(0, len(n_lst) - 1)
