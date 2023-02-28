cases = 10
for x in range(1, cases + 1):
    size = int(input())
    lst = [list(input().split()) for i in range(size)]
    lst_tran = list(zip(*lst))

    gyuchak = 0

    for i in range(size):
        stk = []
        for j in range(size):
            if lst_tran[i][j] == '1':
                if not stk or stk[-1] == '2':
                    stk.append('1')
            elif lst_tran[i][j] == '2':
                if stk and stk[-1] == '1':
                    stk.append('2')

        while stk and stk[-1] == '1':
            stk.pop()


        gyuchak += len(stk) // 2

    print(f'#{x} {gyuchak}')


