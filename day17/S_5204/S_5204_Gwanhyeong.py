def partition(lst):
    # 최소 단위 까지 분할
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = partition(lst[:mid])
    right = partition(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    len_left = len(left)
    len_right = len(right)
    result = []
    l, r = 0, 0
    i = 0
    if left[-1] > right[-1]:
        cnt += 1

    while l < len_left or r < len_right:
        if l < len_left and r < len_right:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l < len_left:
            result.append(left[l])
            l += 1
        elif r < len_right:
            result.append(right[r])
            r += 1
    return result


T = int(input())

for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    data = partition(arr)
    print(f'#{tc} {data[N//2]} {cnt}')