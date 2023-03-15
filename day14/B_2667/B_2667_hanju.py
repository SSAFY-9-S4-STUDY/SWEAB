# 붙어있는 집의 좌표를 DFS를 통해 찾는 함수
# 탐색한 집의 값은 0으로 만들어주어 중복 탐색 방지
# 반환값은 총 탐색된 집의 개수
def next_house(row, col):
    global houses
    stack, cnt = [(row, col)], 0
    while stack:
        x, y = stack.pop()
        cnt += 1
        for v in vector:
            nx, ny = x + v[0], y + v[1]
            if 0 <= nx < N and 0 <= ny < N and houses[nx][ny] == 1:
                stack.append((nx, ny))
                houses[nx][ny] = 0
    return cnt


# 입력값 받기
N = int(input())
houses = [list(map(int, input())) for _ in range(N)]

vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = []

# 이중배열을 탐색하며 집이 나타나면 함수를 통해 붙어있는 집 개수 계산
for r in range(N):
    for c in range(N):
        if houses[r][c] == 1:
            houses[r][c] = 0
            ans.append(next_house(r,c))

# 정답 출력
print(len(ans))
for i in sorted(ans):
    print(i)