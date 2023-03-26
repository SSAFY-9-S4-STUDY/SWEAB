cases = int(input())


def quick_sort(lst, l, r):

    if l < r:
        pivot = lst[l]
        i = l + 1
        j = r
        while i <= j:
            while i <= j and lst[i] <= pivot:
                i += 1
            while i <= j and lst[j] >= pivot:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
        lst[j], lst[l] = lst[l], lst[j]
        quick_sort(lst, l, j - 1)
        quick_sort(lst, j + 1, r)



for x in range(1, cases + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, N - 1)
    print(f'#{x}', lst[N // 2])