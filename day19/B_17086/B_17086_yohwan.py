import sys
sys.stdin = open("input.txt")

from collections import deque

# 상어로부터 얼마나 멀리 떨어져있는지 찾아주는 함수
# 모든 상어 위치에서 방향만큼 1칸씩 동시에 이동한 후 거리 표시
def find():
    queue = deque(shark)
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < M:
                # 비짓이 0이라면 큐에 추가해주고 얼마나 떨어져있는지표시
                if visited[ni][nj] == 0:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = []
# 주석달면서 생각해봤는데 굳이 visited를 넣을 필요없이
# 위에 arr에 그대로 썻어도 됐을 것 같음
# 풀이중에 arr를 재사용하는 과정도 없을 뿐더러 초기 visited랑 arr가 같네
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append((i,j))
            visited[i][j] = 1

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


find()
print(max(map(max, visited))-1 )

