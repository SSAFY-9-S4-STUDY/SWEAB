import sys

N, M = map(int, input().split())

dogam1 = dict()
dogam2 = dict()

for num in range(1, N + 1):
    pocketmon = sys.stdin.readline().rstrip()

    if pocketmon not in dogam1:
        dogam1[pocketmon] = str(num)

dogam2 = dict(map(reversed, dogam1.items()))

ans = []
for _ in range(M):
    new = sys.stdin.readline().rstrip()
    if new in dogam1:
        ans.append(dogam1.get(new))
    else:
        ans.append(dogam2.get(new))

for m in ans:
    print(m)