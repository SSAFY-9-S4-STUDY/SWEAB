# 재귀함수를 이용해서 배열의 값이 1이면 0으로 바꿔서 중복 카운트를 방지하고
# 그 점을 기준으로 4방향으로 1이 추가로 있는지 탐색 
def solution(x,y):
    global cnt
    if (0 <= x < N and 0 <= y < N) and arr[y][x] == 1:
        arr[y][x] = 0
        cnt += 1
        for i, j in DIRECTIONS:
            solution(x+i,y+j)
        return True
    else:
        return False


DIRECTIONS = ((1,0), (-1,0), (0,1), (0, -1))
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []
cnt = 0
for i in range(N):
    for j in range(N):
        if solution(i, j):
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
for char in ans:
    print(char)
