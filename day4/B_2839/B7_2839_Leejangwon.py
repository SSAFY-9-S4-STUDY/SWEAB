# B7_2839

N = int(input())

'''
방향성은 우선 주어진 N과 같아질 수 있는지. 이후, 같다면 1. 5로만 이루어진 거
2. 3으로만 이루어진 거 3. 같이 만들었을 때 이 3개 중 가장 작은 값을 리턴하도록
단, 0은 배제해야
같아지지 않으면 -1을 리턴하도록
'''


min_case = []

# 5로만 이루어질 수 있는지.
m = 0
while 5 * m != N:
    if 5 * m > N:
        m = 0
        break
    m += 1

if m != 0:
    min_case.append(m)

# 3으로만 이루어질 수 있는지.
n = 0
while 3 * n != N:
    if 3* n > N:
        n = 0
        break
    n += 1

if n != 0:
    min_case.append(n)

# 5와 3으로 이루어질 수 있는지.
a = 0   # 5 갯수
b = 0   # 3 갯수

for i in range(N//5 + 1):
    for j in range(N//3 + 1):
        if 5 * i + 3 * j == N:
            a, b = i, j
            min_case.append(a + b)

if min_case != []:
    print(min(min_case))
else:
    print(-1)


# # 배워야하는 코드 방향

# sugar = int(input())

# bag = 0
# while sugar >= 0:
#     if sugar % 5 == 0:
#         bag += (sugar // 5)
#         print(bag)
#         break
#     sugar -= 3
#     bag += 1
# else:
#     print(-1)