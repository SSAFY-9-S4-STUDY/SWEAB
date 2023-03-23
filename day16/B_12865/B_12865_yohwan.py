import sys
sys.stdin = open("input.txt")

# 큐로 만들어서 이렇게 저렇게 해보려고했는데 실패,,
# 그래서 대신 시간초과 메모리초과나는 풀이라도ㅎㅎㅎㅎ
# 먼 입대전에 여행이여 술이나 마셔라 준서야 ㅠ

from itertools import combinations

N, K = map(int, input().split())
things = []
ans = 0
for _ in range(N):
    W, V = map(int, input().split())
    things.append([W, V])
for i in range(1, N):
    bag = list(combinations(things, i))
    weight = 0
    value = 0
    for j in range(len(bag)):
        for k in range(i):
            weight += bag[j][k][0]
            value += bag[j][k][1]
        if weight <= K and ans <= value:
            ans = value
        weight = 0
        value = 0

print(ans)


