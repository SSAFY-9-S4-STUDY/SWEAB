def merge_sort(arr):    # 분할정복 활용 병합 정렬
    global cnt
    if len(arr) == 1:   # 길이가 1일 때 배열을 리턴
        return arr
    mid = (len(arr)) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    l, r = 0, 0
    result = []
    while l < len(left) or r < len(right):
        if l == len(left):
            result.append(right[r])
            r += 1
        elif r == len(right):
            result.append(left[l])
        elif left[l] > right[r]:
            result.append(right[r])
            r += 1
        elif left[l] <= right[r]:
            result.append(left[l])
            l += 1
    return result

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    x = merge_sort(arr)[n // 2]
    print(f'#{tc}', x, cnt)