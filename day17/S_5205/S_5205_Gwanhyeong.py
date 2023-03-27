def quick_sort(left, right):
    if left >= right:
        return
    pivot = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and arr[pivot] >= arr[i]:
            i += 1
        while i <= j and arr[pivot] <= arr[j]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr))
    print(f'#{tc} {arr[N//2]}')