n = int(input())

num_array = [list(map(int,input().split())) for _ in range(n)]

num_array = sorted(num_array)

for point in num_array:
    print(*point)

# 내장함수 안 쓰시고 하는 것도 생각해봤는데 도저히 안 나오네요...
# 하신 분 있으면 알려주셔요~