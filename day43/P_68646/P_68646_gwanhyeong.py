# 아이디어 문제 - 최후까지 남을 수 있는 풍선의 조건이 무엇인가?
# 배열 a 의 해당 element이 해당 element 기준으로 왼쪽 모든 원소보다 작은 값이거나
# 오른쪽 모든 원소보다 작은 값이면 최후로 남을 수 있음.

def solution(a):
    arr = [0] * len(a)
    INF = 1000000001
    left_min, right_min = INF, INF
    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
            arr[i] = 1
        if a[len(a) - i - 1] < right_min:
            right_min = a[len(a)-i-1]
            arr[len(a)-i-1] = 1
    return sum(arr) 