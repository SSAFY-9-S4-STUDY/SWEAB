from itertools import combinations


N, M = map(int,input().split())
cards = list(map(int,input().split()))
max_temp = 0

for j in combinations(cards,3):
    if max_temp <sum(list(j)) <= M:
                max_temp = sum(list(j))

print(max_temp)






