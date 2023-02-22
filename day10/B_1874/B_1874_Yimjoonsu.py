N = int(input())
count = 1
stack = []
arith = []
result = 1

for i in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        arith.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        arith.append('-')
    else:
        result = 0

if result:
    for i in arith:
        print(i)
else:
    print('NO')