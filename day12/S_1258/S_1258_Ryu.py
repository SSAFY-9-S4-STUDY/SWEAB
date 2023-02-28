cases = int(input())
for x in range(1, cases + 1):
    size = int(input())
    lst = [list(map(int,input().split())) for _ in range(size)]

    # 행렬의 개수, 행과 열의 크기(작은 순서대로, 크기가 같으면 행이 작은 순)

    visited = [[0 for _ in range(size)] for _ in range(size)]

    bubun = []

    for i in range(size):
        for j in range(size):
            if lst[i][j] != 0 and visited[i][j] == 0:
                hang = 0
                while i + hang < size and lst[i + hang][j] != 0:
                    hang += 1
                yeul = 0
                while j + yeul < size and lst[i][j + yeul] != 0:
                    yeul += 1

                bubun.append((hang, yeul))

                for i1 in range(i, i + hang):
                    for j1 in range(j, j + yeul):
                        visited[i1][j1] = 1

    bubun.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{x} {len(bubun)}', end=' ')
    for i in bubun:
        print(*i, end=' ')
    print()