# 병합정렬


def merge_sort(raw_arr):
    if len(raw_arr) < 2:
        return raw_arr

    mid = len(raw_arr) // 2
    pre_arr = merge_sort(raw_arr[:mid])
    post_arr = merge_sort(raw_arr[mid:])

    return merge(pre_arr, post_arr)


def merge(left_arr, right_arr):
    global cnt
    merged_arr = []
    left_ = right_ = 0
    if left_arr[-1] > right_arr[-1]:  # 오른쪽이 먼저 복사되는 경우
        cnt += 1
    while left_ < len(left_arr) and right_ < len(right_arr):
        if left_arr[left_] < right_arr[right_]:
            merged_arr.append(left_arr[left_])
            left_ += 1
        else:
            merged_arr.append(right_arr[right_])
            right_ += 1

    while left_ < len(left_arr):
        merged_arr.append(left_arr[left_])
        left_ += 1
    while right_ < len(right_arr):
        merged_arr.append(right_arr[right_])
        right_ += 1

    return merged_arr


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(lst)
    print(f'#{tc} {ans[n//2]} {cnt}')