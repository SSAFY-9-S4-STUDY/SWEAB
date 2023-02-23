n = int(input())
arr = [int(input()) for _ in range(n)]

quest = [i + 1 for i in range(n)]

cal = ''

stack = []
j = 0
for i in range(1, n + 1):
    stack.append(i)
    cal += '+\n'
    while i == arr[j]:
        stack.pop()
        cal += '-\n'
        j += 1
        if stack:
            i = stack[-1]
        else:
            break
        if j > n:
            break
    if j > n:
        break

if stack:
    print("NO")
else:
    print(cal)
