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
            if len(lst1[idx1]) < len(lst2[idx2]):
                res[total_idx] = lst1[idx1]
                idx1 += 1
                total_idx += 1
            elif len(lst1[idx1]) > len(lst2[idx2]):
                res[total_idx] = lst2[idx2]
                idx2 += 1
                total_idx += 1
            else:
                if sort_words(lst1[idx1],lst2[idx2]):
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
    else:
        return merging(merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:]))

# 단어 정렬 함수
def sort_words(w1, w2):
    for i,j in zip(w1,w2):
        if ord(i) < ord(j):
            return True
        elif ord(i) > ord(j):
            return False
    return True
        

import sys
N = int(sys.stdin.readline())

words = set([sys.stdin.readline().replace('\n','') for i in range(N)])
print('\n'.join(merge_sort(list(words))))



