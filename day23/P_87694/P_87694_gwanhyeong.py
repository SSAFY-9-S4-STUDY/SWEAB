from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # characterX ~ itemY 는 1부터 50 사이의 자연수이므로 인덱스를 맞추고
    # 2배를 해줘서 51 * 2 = 102 까지 field 생성
    field = [[-1] * 102 for i in range(102)]

    for r in rectangle:
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda element: element * 2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형의 내부라면 0 으로 바꾸고
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리이면 1로 바꾼다.
                elif field[i][j] != 0:
                    field[i][j] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]
    # 아직 방문하지 않은 곳은 1로 표시
    visited[characterX * 2][characterY * 2] = 0
    # 시작 지점은 0으로 초기화
    answer = 0
    while q:
        x,y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 아니라면 상하좌우 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if field[nx][nx] == 1 and visited[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer