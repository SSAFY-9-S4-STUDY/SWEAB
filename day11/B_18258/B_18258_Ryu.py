import sys
input = sys.stdin.readline

q = [0] * 2000000
front = -1
back = -1
num = int(input())

for i in range(num):
    order, *num = input().strip().split()

    if order == 'push':
        back += 1
        q[back] = num[0]

    elif order == 'pop':
        if front == back:
            print(-1)
        else:
            front += 1
            print(q[front])

    elif order == 'size':
        print(back - front)

    elif order == 'empty':
        if front == back:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if front == back:
            print(-1)
        else:
            print(q[front + 1])

    elif order == 'back':
        if front == back:
            print(-1)
        else:
            print(q[back])
