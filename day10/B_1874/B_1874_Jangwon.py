import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(range(n, 0, -1))
my_stack = [0]
result = []
status = True
for _ in range(n):
    m = int(input())
    while my_stack[-1] != m:
        if num:
            my_stack.append((num.pop()))
            result.append('+')
        else:
            break
    item = my_stack.pop()
    if item == m:
        result.append('-')
    else:
        status = False

if status:
    for c in result:
        print(c)
else:
    print('NO')