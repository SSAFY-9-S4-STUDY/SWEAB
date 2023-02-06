t = int(input())

ground = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y+10):
            ground[j][i] = 1


rst = sum(sum(ground, []))
print(rst)