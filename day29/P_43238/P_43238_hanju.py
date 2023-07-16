def solution(n, times):
    # 입력된 시간에 해당하는 승객 수를 반환하는 함수
    def assign(second):
        return sum([second // t for t in times])
    
    # 이진 탐색을 통해 최소 시간을 반환하는 함수
    def binary_search(L, R):
        print(L, R)
        M = (L+R)//2
        now, small = assign(M), assign(M-1)
        print(now, small)
        # 현재 입력시간이 최소인 경우
        if now == n and small < n-1:
            return M
        # 현재 입력된 시간이 최소보다 클 경우
        elif small >= n:
            return binary_search(L, M)
        # 현재 입력된 시간이 부족할 경우
        elif now <= n-1:
            return binary_search(M, R)
    
    return binary_search(0, min(times) * n)

print(solution(1, [1, 1]))
    
    