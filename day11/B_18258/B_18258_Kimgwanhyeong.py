# 이렇게 풀면 시간초과
# import sys
# input = sys.stdin.readline 하면 출력이 안됨...
from collections import deque

N = int(input())

queue = deque([])
for _ in range(N):
    check = input()
    if 'push' in check:
        queue.append(int(check[5:]))
    
    elif check == 'pop':
        if queue:
            item = queue.popleft()
            print(item)
        else:
            print('-1')
    
    elif check == 'size':
        print(len(queue))
    
    elif check == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    
    elif check == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    
    elif check == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')