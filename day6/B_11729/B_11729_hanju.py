def hanoi(n,start,end,tmp):
    if n == 1:
        print(start,end)
    else:
        hanoi(n-1,start,tmp,end), hanoi(1,start,end,tmp), hanoi(n-1,tmp,end,start)

N = int(input())

print(2**N-1)
hanoi(N,1,3,2)


