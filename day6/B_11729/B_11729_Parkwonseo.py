# 하노이탑
"""
f(n + 1) = 2f(n) + 1
1 == "1 3"
f(n) = "처음의 기둥에서 다른 기둥으로" n개의 원판을 옮기는 최소의 횟수
f(n, i, j) = i번째 기둥에서 j번째 기둥으로 n개의 원판을 옮기는 최소의 횟수
f(n+1, i, j) = f(n, i, 3-i-j) + f(1, i, j) + f(n, 3-i-j, j)
0 <= i, j <= 2, k
i != j
i + j + k = 3
3 - i - j = k
f(n) = f(n-1) + f(n-1) + f(1)
    = {f(n-2) + f(n-2) + f(1)} + {f(n-2) + f(n-2) + f(1)} + f(1)
f1 = 1                      1 3
f2 = 2*1 + 1                1 2, '1 3', 2 3
f3 = 2*f2 + 1               1 3, 1 2, 3 2, '1 3', 2 1, 2 3, 1 3
    = 2*(2*1 + 1) + 1
f4                          1 2, 1 3, 2 3, 1 2, 3 1, 3 2, 1 2, `1 3`,
                            2 3, 2 1, 3 1, 2 3, 1 2, 1 3, 2 3
"""

N = int(input())

def hanoi(tower, i, j):
    if tower == 1:
        print(f"{i+1} {j+1}")
        return 1
    tower -= 1
    return hanoi(tower, i, 3-i-j) + hanoi(1, i, j) + hanoi(tower, 3-i-j, j)

print(hanoi(N, 0, 2))
