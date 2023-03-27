def merge_sort(arr):
    global cnt
    n = len(arr)
    # 정렬할 리스트의 개수가 한 개 이하면 리턴
    if n<= 1:
        return arr
    
    # 중간을 기준으로 두 그룹으로 나눔
    mid = n // 2
    g1 = arr[:mid]
    g2 = arr[mid:]
    # 재귀
    g1 = merge_sort(g1)
    g2 = merge_sort(g2)
    if g1[-1] > g2[-1]:
        cnt += 1
    
    # 병합 과정
    result = []
    
    # g1과 g2에 인자가 남아있을때 작은 값을 결과에 추가
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    # 둘중에 한 곳에만 인자가 남아있을때 결과에 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)[N // 2]
    
    print(f'#{test_case} {ans} {cnt}')