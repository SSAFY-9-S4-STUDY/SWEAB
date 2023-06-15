def solution(beginning, target):
    N, M = len(beginning), len(beginning[0])
    difference = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            difference[r][c] = abs(target[r][c] - beginning[r][c])

    return difference

beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

from pprint import pprint
pprint(solution(beginning, target))