T = int(input())
for i in range(T):
    M = input()

    r = 1
    result = 0
    for j in M: #"OO XX O XX OOO"
        if j == 'O':
            result += r
            r += 1
        else:
            r = 1

    print (result)