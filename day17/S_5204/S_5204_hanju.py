def merge_sort(arr1, arr2, n1, n2):
    global cnt
    if arr1[-1] > arr2[-1]:
        cnt += 1

    rst = []
    idx1 = idx2 = 0

    while idx1 != n1 and idx2 != n2:
        if arr1[idx1] <= arr2[idx2]:
            rst.append(arr1[idx1])
            idx1 += 1
        else:
            rst.append(arr2[idx2])
            idx2 += 1

    if idx1 == n1:
        rst += arr2[idx2:]
    else:
        rst += arr1[idx1:]
    
    return rst


def merge(arr, n):
    if n < 2:
        return arr
    else:
        n1, n2 = n//2, n - n//2
        return merge_sort(merge(arr[:n//2], n1), merge(arr[n//2:], n2), n1, n2)


T = int(input())

for test_case in range(1 ,T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    print(f'#{test_case} {merge(nums, N)[N//2]} {cnt}')