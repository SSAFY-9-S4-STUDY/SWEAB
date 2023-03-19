dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def danji(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 0:
        return 0

    arr[x][y] = 0
    count += 1

    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        danji(new_x, new_y)

    return count


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []
count = 0

for i in range(N):
    for j in range(N):
        temp = danji(i, j)
        if temp:
            result.append(temp)
            count = 0

print(len(result))
result.sort()
for num in result:
    print(num)