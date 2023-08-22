def solution(key, lock):
    # 1. 변수 할당 및 조작
    # 각 배열의 크기들
    N, M = len(lock), len(key)
    # 자물쇠에 있는 홈에 개수
    num_zero = N**2 - sum(sum(lock,[]))
    # 비교하기 쉽게 key 0과 1 바꾸기
    key_reverse = [list(map(lambda x: abs(x-1), row)) for row in key]

    # 2. 자물쇠를 회전시키며 열쇠와 비교
    for _ in range(4):
        # 자물쇠 회전
        lock = [list(row) for row in zip(*lock[::-1])]
        print(lock)
        # 모든 자물쇠의 부분을 탐색
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                # 자물쇠 부분의 크기에 부합하는 열쇠 부분
                key_part = [row[max(0, M - 1- j) : min(M, N + M - 1 - j)] for row in key_reverse[max(0, M - 1- i) : min(M, N + M - 1 - i)]]
                lock_part = [row[max(0, j - M + 1) : min(N, j + 1)] for row in lock[max(0, i - M + 1) : min(N, i + 1)]]
                if key_part == lock_part

    return num_zero


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# # print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1,1,1,1,1],[1,1,0,1,1],[1,0,1,0,1],[1,1,0,1,1],[1,1,1,1,1]]))
