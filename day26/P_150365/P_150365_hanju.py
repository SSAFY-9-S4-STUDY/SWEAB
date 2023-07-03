from collections import deque
import sys

sys.setrecursionlimit(1000000)

def solution(n, m, x, y, r, c, k):
    # 방향과 경로명을 매칭한 딕셔너리
    dircetions = {(1,0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0): 'u'}

    # 미로 탐색 함수
    def search(x, y, k, route):
        # 도착시 경로를 반환
        if k == 0 and x == r and y == c:
            return route
        # 도착할 수 없는 경우 불가능을 반환
        distance = abs(r-x) + abs(c-y)
        if distance > k or (k-distance) % 2:
            return 'impossible'
        # 그 외의 경우 사전 순으로 탐색 진행
        for i, j in dircetions:
            new_x, new_y = x + i, y + j
            if 0 < new_x <= n and 0 < new_y <= m:
                result = search(new_x, new_y, k - 1, route + dircetions.get((i, j)))
                if result != 'impossible':
                    return result

    # dfs로 미로를 순회
    return search(x,y,k, '')

print(solution(3,4,2,3,3,1,1))