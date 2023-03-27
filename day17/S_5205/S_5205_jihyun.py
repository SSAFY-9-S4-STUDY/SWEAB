def quick(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, n):
        if pivot >= arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick(left) + [pivot] + quick(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    A = quick(lst)
    print(f'#{tc} {A[N//2]}')