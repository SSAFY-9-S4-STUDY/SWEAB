def merge(lst1):
    if len(lst1) == 1:
        return lst1
    global count
    mid = len(lst1) // 2
    left = merge(lst1[:mid])
    right = merge(lst1[mid:])

    len_L = len(left)
    len_R = len(right)

    idx = idx_L = idx_R = 0

    while idx_L < len_L and idx_R < len_R:
        if left[idx_L] <= right[idx_R]:
            lst1[idx] = left[idx_L]
            idx_L += 1
        else:
            lst1[idx] = right[idx_R]
            idx_R += 1
        idx += 1

    if idx_L == len_L:
        for i in range(idx_R, len_R):
            lst1[idx] = right[i]
            idx += 1
    elif idx_R == len_R:
        count += 1
        for i in range(idx_L, len_L):
            lst1[idx] = left[i]
            idx += 1
    return lst1


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    count = 0
    print(f'#{test_case} {merge(lst)[N//2]} {count}')
# https://cys4585.tistory.com/20
