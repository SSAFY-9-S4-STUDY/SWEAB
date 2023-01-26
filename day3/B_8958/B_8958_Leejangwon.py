T = int(input())

for i in range(T):
    c = input()
    total = 0

    count = 0
    for j in c:
        if j == 'O':
            count += 1
            total += count
        if j == 'X':
            count = 0
    
    print(total)

