def solution(key, lock):
    # 1. 변수 할당 및 조작
    # 각 배열의 크기들
    N, M = len(lock), len(key)
    # 자물쇠에 있는 홈에 개수
    num_zero = N**2 - sum(sum(lock,[]))
    # 비교하기 쉽게 key 0과 1 바꾸기
    lock_reverse = [list(map(lambda x: abs(x-1), row)) for row in lock]

    # 2. 자물쇠를 회전시키며 열쇠와 비교
    for _ in range(4):
        # 자물쇠 회전
        lock_reverse = [list(row) for row in zip(*lock_reverse[::-1])]
        # 모든 자물쇠의 부분을 탐색
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                # 자물쇠 부분의 크기에 부합하는 열쇠 부분
                key_part = [row[max(0, M - 1- j) : min(M, N + M - 1 - j)] for row in key[max(0, M - 1- i) : min(M, N + M - 1 - i)]]
                # 열쇠 부분의 위치와 크기에 맞춰 자른 자물쇠의 부분
                lock_part = [row[max(0, j - M + 1) : min(N, j + 1)] for row in lock_reverse[max(0, i - M + 1) : min(N, i + 1)]]
                # 모든 조건이 맞다면 True를 반환
                if key_part == lock_part and sum(sum(key_part,[])) == num_zero:
                    return True

    # 조건에 맞는 부분이 없다면 False를 반환
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))