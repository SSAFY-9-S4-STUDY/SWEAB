cases = int(input())


def merge_sort(lst):
    global cnt
    leng = len(lst)
    if leng <= 1:
        return lst

    mid = leng // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt += 1

    rlt = [0] * leng
    index = 0
    li = 0
    ri = 0
    while li != mid and ri != leng - mid:
        if left[li] < right[ri]:
            rlt[index] = left[li]
            li += 1
        else:
            rlt[index] = right[ri]
            ri += 1
        index += 1
    if li != mid:
        for i in range(index, len(lst)):
            rlt[i] = left[li]
            li += 1
    else:
        for i in range(index, len(lst)):
            rlt[i] = right[ri]
            ri += 1

    return rlt


for x in range(1, cases + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f'#{x}', lst[N//2], cnt, lst)