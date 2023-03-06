t = int(input())
for tc in range(1, t + 1):
    n, submit_num = map(int, input().split())
    submit = list(map(int, input().split()))
    lst = [0] * (n + 1)
    for good in submit:
        lst[good] = 1
    
    print(f"#{tc} ", end='')
    for i in range(1, n + 1):
        if lst[i] == 0:
            print(i, end=' ')
    print()