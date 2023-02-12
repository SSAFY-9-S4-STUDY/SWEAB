import sys
from math import gcd

n = int(sys.stdin.readline())
ls = []
result = []

for _ in range(n):
    ls.append(int(sys.stdin.readline()))
ls.sort()

temp = [ls[i] - ls[i - 1] for i in range(1, n)]
my_gcd = temp[0]

for i in range(1, n - 1):
    my_gcd = gcd(my_gcd, temp[i])

for i in range(1, int(pow(my_gcd, 1 / 2)) + 1):
    if my_gcd % i == 0:
        if i ** 2 == my_gcd:
            result.append(i)
        else:
            result += [i, my_gcd // i]
result.remove(1)
result.sort()

for i in range(len(result)):
    print(result[i], end=' ')


# 유클리드 호제법을 모를 때
# inspection = list(map(int, inspection))
# K = min(inspection)
#
# for i in range(2, K):
#     tmp = set(map(lambda x: x % i, inspection))
#     if len(tmp) == 1: ans.append(i)

# (1)번 풀이
import sys
#
# # 문제 입력
# N = int(sys.stdin.readline().strip())
# inspection = [int(sys.stdin.readline()) for _ in range(N)]
# re_num = []
#
# for i in range(1, N):
#     re_num.append(inspection[i] - inspection[i-1])
#
#
# # 유클리드 호제법
# def findGCD(a, b):
#     num = b
#     div = a
#     rest = num % div
#     while rest != 0:
#         num = div
#         div = rest
#         rest = num % div
#     return div
#
# GCD = re_num[0]
# for idx in range(1, len(re_num)):
#     GCD = findGCD(GCD, re_num[idx])
#
# result = set()
# for i in range(2, int(GCD**0.5) + 1):
#     if GCD % i == 0:
#         result.add(i)
#         result.add(GCD // i)
# result.add(GCD)
#
# print(*sorted(list(result)))