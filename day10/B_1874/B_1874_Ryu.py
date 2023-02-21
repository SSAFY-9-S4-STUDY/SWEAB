import sys
input = sys.stdin.readline

num = int(input())
suyeul = [int(input()) for _ in range(num)]
numbers = list(range(1, num + 1))
stk = []

ans = []
n = 0
for i in numbers:
    stk.append(i)
    ans.append('+')
    while stk and stk[-1] == suyeul[n]:
        n += 1
        stk.pop()
        ans.append('-')

if stk:
    print('NO')
else:
    print('\n'.join(ans))