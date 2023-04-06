def paper(x, y, n):
    visited = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != visited:
                for a in range(3):
                    for b in range(3):
                        paper(x + a*n//3, y + b*n//3, n//3)
                return

    result[visited] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 3
paper(0, 0, N)

print(result[-1])
print(result[0])
print(result[1])