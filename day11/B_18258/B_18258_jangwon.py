from collections import deque

import sys
N = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(N):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[-1])