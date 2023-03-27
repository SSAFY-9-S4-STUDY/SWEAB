"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    pre_arr, mid_arr, post_arr = [], [], []
    for num in arr:
        if num < pivot:
            pre_arr.append(num)
        elif num > pivot:
            post_arr.append(num)
        else:
            mid_arr.append(num)
    return quick_sort(pre_arr) + quick_sort(mid_arr) + quick_sort(post_arr)
"""


def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot, tail = array[0], array[1:]

    pre_arr = [x for x in tail if x <= pivot]
    post_arr = [x for x in tail if x > pivot]

    return quick_sort(pre_arr) + [pivot] + quick_sort(post_arr)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    raw_lst = list(map(int, input().split()))
    sorted_lst = quick_sort(raw_lst)
    print(f"#{tc} {sorted_lst[n // 2]}")

# 마지막 테스트케이스 제한시간 초과