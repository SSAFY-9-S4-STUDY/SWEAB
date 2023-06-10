def dfs(x, y, res, cnt):
    global answer
    dir = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
    # [0] 백트래킹
    if cnt < abs(x-R) + abs(y-C):
        return
    # [1] 도착하면?
    if cnt == 0:
        if (x, y) == (R, C):
            answer = res
        return
    # [2] 아직 도착 안했다면?
    for dx, dy, key in dir:
        if 0 < x+dx <= N and 0 < y+dy <= M and res+key < answer:
            dfs(x+dx, y+dy, res+key, cnt-1)


def solution(n, m, x, y, r, c, k):
    global R, C, N, M, answer
    R, C, N, M, answer = r, c, n, m, 'z'

    # [1] impossible 여부 확인
    distance = abs(x-r) + abs(y-c)
    if k < distance or (k - distance) % 2:
        return "impossible"
    # [2] dfs
    dfs(x, y, '', k)

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1,	2, 3, 3, 4))
