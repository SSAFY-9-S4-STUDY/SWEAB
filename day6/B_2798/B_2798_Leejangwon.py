N, M = map(int, input().split())

num_list = list(map(int, input().split()))

temp = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            temp.append(num_list[i] + num_list[j] + num_list[k])
max = 0
for i in range(len(temp)):
        if temp[i] <= M and temp[i] > max:
            max = temp[i]

print(max)