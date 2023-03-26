def quick(left, right):
    if left >= right:
        return

    pivot = left
    i = left+1
    j = right-1

    while i <= j:
        while i <= j and lst[pivot] >= lst[i]:
            i += 1
        while i <= j and lst[pivot] <= lst[j]:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[pivot], lst[j] = lst[j], lst[pivot]
    quick(left, j)
    quick(j + 1, right)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick(0, len(lst))

    print(f'#{test_case} {lst[N//2]}')