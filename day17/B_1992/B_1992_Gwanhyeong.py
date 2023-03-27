## Googling

def dfs(x, y, n):
    check = arr[x][y]
    # NxN 배열 중 하나라도 다른 값이 있다면 check 변수를 -1로 바꿔줌
    for i in range(x,x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                check = -1
                break

    # NxN 배열 중 하나라도 다른 값 있을 때 분할 정복
    if check == -1:
        print('(', end='')
        n = n // 2
        # 왼쪽 상단
        dfs(x,y,n)
        # 오른쪽 상단
        dfs(x,y+n,n)
        # 왼쪽 하단
        dfs(x+n,y,n)
        # 오른쪽 하단
        dfs(x+n, y+n, n)
        print(')', end='')

    # NxN arr 배열 모든 값이 1이라면 1을 출력
    elif check == 1:
        print(1, end='')

    # NxN arr 배열 모든 값이 0이라면 0을 출력
    else:
        print(0, end='')


N = int(input())

arr = [list(map(int,input())) for _ in range(N)]

dfs(0,0,N)