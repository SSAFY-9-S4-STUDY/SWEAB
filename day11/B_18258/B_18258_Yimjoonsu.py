import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([])
count = 0

for _ in range(N):
    exp = input().split()
    term = exp[0]
    if term == 'push':
        queue.append(exp[1])
        count += 1

    elif term == 'pop':
        if queue:
            print(queue.popleft())
            count -= 1
        else:
            print(-1)

    elif term == 'size':
        print(count)

    elif term == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif term == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif term == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)