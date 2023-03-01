import sys
sys.stdin = open("input_1258.txt")


# 1. 사각형 내부 0 없음
# 2. 각 사각형 크기 다 다름 -> 행(y 축 길이)은 행끼리, 열(x축 길이)은 열끼리 모두 무조건 다르다고 함.
# 3. 용기 사이에 상하좌우로는 최소 1칸 떨어져 있다.

t = int(input())
for tc in range(1, t + 1):
    n = int(input())  # storage 정사각형의 한 변 길이
    storage = [list(map(int, input().split())) for _ in range(n)]

    col = dict()  # key = x(col), value = y(row)
    for y in range(n):
        count = 0
        for x in range(n):

            if storage[y][x] != 0:
                count += 1
            elif x == n - 1 or storage[y][x] == 0:
                if count > 0 and col.get(count):
                    col[count] += 1
                elif count > 0:
                    col[count] = 1
                count = 0

    # 정답 => 총 용기(box) 개수, 각 box의 크기(행 * 열)가 작은 순, 크기가 같다면 행이 작은 순

    col = dict(sorted(col.items(), key = lambda x: x[0]))

    result = []  # ( key값(x 크기), value 값(y 크기), 용기 크기 )
    # print(col)
    for elem in col.items():
        tmp = elem[0] * elem[1]
        result.append((elem[0], elem[1], tmp))
    result.sort(key = lambda x: (x[2], x[1]))
    # print(result)

    print(f"#{tc} {len(col)} ", end='')
    for i in range(len(col)):
        print(f"{result[i][1]} {result[i][0]}", end=' ')
    print()
