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

'''
sys.stdin.readline()을 사용하지 않으면 시간초과가 나옵니다.
사용하지 않는다면 stk = []에서 append, pop하는 방법이 아니라
stk = [0 for _ in range(num)]  top = -1을 활용해야합니다.
시간초과가 뜨지는 않는데 4000ms 나옵니다...
'''