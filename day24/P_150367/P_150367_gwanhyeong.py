# 문제를 이해하기도 어려웠다.
from math import log2

def solution(numbers):
    answer = []

    # 해당 2진수를 이진트리 형태로 만들 수 있는지 확인하는 함수
    def check_tree(bin_num):
        length = len(bin_num)
        if length <= 1:
            return bin_num
        else:
            mid = length//2
            # 중앙값이 1이라면 해당 값을 고정하고 나머지 부분을 재귀함수 형태로 check
            if bin_num[mid]=='1':
                return check_tree(bin_num[:mid])+bin_num[mid]+check_tree(bin_num[mid+1:])
            # 중앙값이 0이라면 이후 더 이상 트리를 만들 수 없으므로(더미노드) 
            else:
                return '0' * length

    for num in numbers:
        # 포화이진트리는 2^(높이+1) - 1 개의 노드를 가지므로
        # num 을 이진수로 바꾼 뒤 포화이진트리로 만들기
        before_bin = bin(num)[2:]
        l = len(before_bin)
        height = int(log2(l)) + 1
        new_l = 2**height - 1
        # 포화이진트리를 만들기 위해 부족한 노드의 개수만큼 '0'을 왼쪽에 추가
        after_bin = '0' * (new_l - l) + before_bin
        if after_bin == check_tree(after_bin):
            answer.append(1)
        else:
            answer.append(0)
    return answer
