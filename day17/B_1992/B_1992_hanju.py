def quad_tree(arr, n):
    if N == 1:
        return arr[0][0]
    elif 1 not in sum(arr,[]):
        return 0
    elif 0 not in sum(arr,[]):
        return 1
    else:
        nn = n//2
        UL = quad_tree([arr[i][:nn] for i in range(nn)], nn)
        UR = quad_tree([arr[i][nn:] for i in range(nn)], nn)
        DL = quad_tree([arr[i][:nn] for i in range(nn,n)], nn)
        DR = quad_tree([arr[i][nn:] for i in range(nn,n)], nn)
        return f'({UL}{UR}{DL}{DR})'


N = int(input())
data = [list(map(int,input())) for _ in range(N)]

print(quad_tree(data, N))