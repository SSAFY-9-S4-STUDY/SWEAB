import sys
from collections import deque

N = int(sys.stdin.readline())

queue, size = deque(), 0
for _ in range(N):
    oper = sys.stdin.readline().split()
    act = oper[0]

    if act == 'push':
        queue.append(oper[1])
        size += 1

    elif act == 'size':
        print(size)
        
    elif act == 'empty':
        print(0 if size else 1)

    elif size == 0:
        print(-1)

    elif act == 'pop':
        print(queue.popleft())
        size -= 1

    elif act == 'front':
        print(queue[0])

    else:
        print(queue[-1])
