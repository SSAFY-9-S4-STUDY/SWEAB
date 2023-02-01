area = [[0]*100 for i in range(100)]

N = int(input())
for i in range(N):
    x, y = map(int,input().split())
    for j in range(x, x+10):
        for k in range(y,y+10):
            area[k][j] = 1
print(sum(area,[]).count(1))
