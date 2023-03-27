def merge(arr, N):
    global cnt_right
    if N < 2:
        return arr

    division = N // 2
    left = merge(arr[:division], division)
    right = merge(arr[division:], N - division)

    if left[-1] > right[-1]:
        cnt_right += 1

    merged = []
    l, r = 0, 0
    left_len, right_len = len(left), len(right)
    while l < left_len and r < right_len:
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    if l == left_len:
        merged += right[r:]
    else:
        merged += left[l:]
    return merged


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt_right = 0
    merged = merge(lst, N)
    print(f'#{tc} {merged[N//2]} {cnt_right}')