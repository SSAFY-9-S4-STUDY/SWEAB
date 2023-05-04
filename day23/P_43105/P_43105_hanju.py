def solution(triangle):
    depth = len(triangle)
    for r in range(1, depth):
        previous = [0] + triangle[r-1] + [0]
        for c in range(r+1):
            triangle[r][c] += max(previous[c], previous[c+1])

    return max(triangle[depth-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

        