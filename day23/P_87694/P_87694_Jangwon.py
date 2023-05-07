from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[-1 for _ in range(102)] for _ in range(102)]
    # 초기세팅 시작(모서리는 2, 내부는 1, 차있으면 추가하지 않는 방식)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda t: t * 2, r)
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1):
                if y1 < j < y2 and x1 < i < x2:
                    arr[j][i] = 1
                elif arr[j][i] != 1:
                    arr[j][i] = 2

    answer = 0
    # bfs로 해결하자
    queue = deque([(characterX * 2, characterY * 2)])
    visited[characterY*2][characterX*2] = 0

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            answer = visited[y][x] // 2
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 <= nx < 102 and 0 <= ny < 102) and arr[ny][nx] == 2 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([nx, ny])

    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))