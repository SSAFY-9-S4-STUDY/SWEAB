N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))

cnt = 0
current_end = 0
for i in range(N):
    if arr[i][0] >= current_end:
       cnt+=1
       current_end = arr[i][1]

print(cnt)