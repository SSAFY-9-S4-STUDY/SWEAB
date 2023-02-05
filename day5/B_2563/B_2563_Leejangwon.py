paper_cnt = int(input())

# 100 * 100 행렬 생성
white = [[0 for i in range(100)] for j in range(100)]

# 색종이에 해당되는 부분 1로 채우기
for paper in range(paper_cnt):
    X, Y = map(int, input().split())
    X = X - 1
    Y = Y - 1
    for y in range(Y, Y + 10):
        for x in range(X, X + 10):
            if white[y][x] != 1:
                white[y][x] = 1

# 넓이 구하기
ans = sum(list(map(sum, white)))

print(ans)
