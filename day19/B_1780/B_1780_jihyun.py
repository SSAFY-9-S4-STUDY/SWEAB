def number_count(row, col, n):
    global ans

    if n == 1:
        ans[arr[row][col] + 1] += 1
        return
    
    value = arr[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if arr[i][j] != value:
                # 숫자가 다르면 재귀하고 함수 종료
                n //= 3
                for k in range(3):
                    for l in range(3):
                        number_count(row + k*n, col + l*n, n)
                return
    
    # for문 다 돌았으면
    ans[value + 1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * 3
number_count(0, 0, N)
print(*ans, sep='\n')