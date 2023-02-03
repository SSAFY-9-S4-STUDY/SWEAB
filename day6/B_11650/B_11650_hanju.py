# 병합 정렬 함수 선언 구간입니다.

# 두 정렬된 리스트가 들어오면 합쳐주는 함수
def merging(lst1, lst2):
    
    idx1 = idx2 = 0
    end1, end2 = len(lst1), len(lst2)
    total_idx, res = 0, [0]*(end1+end2)

    while idx1 != end1 or idx2 != end2:
        if idx1 == end1:
            res[total_idx] = lst2[idx2]
            idx2 += 1
            total_idx += 1
        elif idx2 == end2:
            res[total_idx] = lst1[idx1]
            idx1 += 1
            total_idx += 1
        else:
            if (lst1[idx1][0] < lst2[idx2][0]) or (lst1[idx1][0] == lst2[idx2][0] and lst1[idx1][1] < lst2[idx2][1]):
                res[total_idx] = lst1[idx1]
                idx1 += 1
                total_idx += 1
            else:
                res[total_idx] = lst2[idx2]
                idx2 += 1
                total_idx += 1
    return res

# 함수를 반으로 쪼개서 각자 정렬시키는 재귀 함수
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if (lst[0][0] < lst[1][0]) or (lst[0][0] == lst[1][0] and lst[0][1] < lst[1][1]):
            return [lst[0],lst[1]]
        else:
            return [lst[1],lst[0]]
    else:
        return merging(merge_sort(lst[:len(lst)//2+1]), merge_sort(lst[len(lst)//2+1:]))

import sys

N = int(sys.stdin.readline())
xy = [0]*N

for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    xy[i] = (x,y)

# 정렬한 좌표들을 언패킹하여 출력
for i in merge_sort(xy):
    print(*i)

