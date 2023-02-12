import math

n = int(input())
quest = [0] * n
for i in range(n):
    quest[i] = int(input())
    # n개의 수에 대한 공약수들을 구해야 한다..
quest.sort()
ans = set()
# for i in range(2, quest[1]):
#     for j in range(n - 1):
#         if quest[j] % i != quest[j + 1] % i:
#             break
#     else: ans.add(i)

# print(*ans)

diff = []
for i in range(1, n):
    diff.append(quest[i] - quest[0])

gcd = math.gcd(*diff)
for i in range(1, int(gcd) // 2 + 1):
    if gcd % i == 0:
        ans.add(i)

for i in sorted(ans)[1:]:
    print(i)
print(gcd)

# quest[0]과 나머지 elem 들의 차(나머지 지우기)의 집합에 공약수들을 구하면 됨.
# 위 차들의 집합에 최대 공약수를 구한 뒤 그 약수를 구해줌.
# 꼭 q[0]일 필요는 없고, 그냥 기준 하나 잡고 모든 elem들을 비교만 하면 됨.