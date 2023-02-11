import sys
input = sys.stdin.readline

def factorial(num):  # 팩토리얼 함수
    res = 1
    for i in range(1, num + 1): res *= i
    return res

def Combination(n, r):  # 조합 함수
    res = factorial(n) / factorial(r) / factorial(n - r)
    return int(res)


N, K = map(int, input().split())
print(Combination(N, K) % 10007)  # 이항계수를 10,007로 나눈 나머지 출력
