def solution(key, lock):
    M = len(key)
    N = len(lock)
    target = []

    # [0] 새로운 자물쇠 만들기... 기존 자물쇠에 두께 M만큼 패딩하기
    new_lock = [[0] * (2 * M + N) for _ in range(2 * M + N)]

    for i in range(M, N + M):
        for j in range(M, N + M):
            new_lock[i][j] = lock[i - M][j - M]

    # [1] 자물쇠 빈칸 좌표 저장
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                target.append((i + M, j + M))

    # [2] 브루트 포스
    for i in range(M + N):
        for j in range(M + N):
            pass

    return False


def putKeyIn(i, j, key, new_lock):
    M = len(key)

    for ki in range(i, i + M):
        for kj in range(j, j + M):



print(solution([[0, 0, 1], [0, 0, 1], [0, 1, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
