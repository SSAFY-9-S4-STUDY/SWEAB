N = int(input())
target = [int(input()) for _ in range(N)]
target.reverse()

rst, stack, i = [], [], 1

while target:

    if i <= target[-1]:
        stack.append(i)
        rst.append('+')
        i += 1

    elif stack[-1] == target[-1]:
        stack.pop()
        target.pop()
        rst.append('-')
        
    else:
        rst = ['NO']
        break

for i in rst:
    print(i, end='\n')



