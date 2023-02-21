import sys
input = sys.stdin.readline

num = int(input())

suyeul = [int(input()) for _ in range(num)]
front = 0

numbers = list(range(1, num + 1))

stk = [0] * num
idx = -1

ans = []

for i in numbers:
    idx += 1
    stk[idx] = i
    ans.append('+')
    while idx != -1 and stk[idx] == suyeul[front]:
        front += 1
        idx -= 1
        ans.append('-')

if idx != -1:
    print('NO')
else:
    print('\n'.join(ans))