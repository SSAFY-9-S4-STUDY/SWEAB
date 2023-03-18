import sys
from collections import deque

input = sys.stdin.readline

case = 1
while True:

    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    visited = [0] * N
    lst = [[] for _ in range(N)]
    for i in range(M):
        n1, n2 = map(int, input().split())
        lst[n1 - 1].append(n2 - 1)
        lst[n2 - 1].append(n1 - 1)

    connected = []
    for i in range(N):
        if visited[i] == 0:
            temp = [i]
            stk = deque([i])
            visited[i] = 1
            while stk:
                cur = stk.pop()
                for j in lst[cur]:
                    if visited[j] == 0:
                        visited[j] = 1
                        stk.append(j)
                        temp.append(j)
            connected.append(temp)

    rlt = 0
    for cnd in connected:
        lines = 0
        for i in cnd:
            lines += len(lst[i])
        if len(cnd) == lines // 2 + 1:
            rlt += 1

    if rlt > 1:
        print(f'Case {case}: A forest of {rlt} trees.')
    elif rlt == 1:
        print(f'Case {case}: There is one tree.')
    elif rlt == 0:
        print(f'Case {case}: No trees.')

    case += 1