from collections import deque
import sys


t = int(sys.stdin.readline())
queue = deque()
for tc in range(t):
    quest = sys.stdin.readline().split()

    if quest[0] == 'push':
        queue.append(quest[1])

    elif quest[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif quest[0] == 'size':
        print(len(queue))

    elif quest[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif quest[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif quest[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
