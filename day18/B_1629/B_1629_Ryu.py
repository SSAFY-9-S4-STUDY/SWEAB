from collections import deque
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
seed = a % c
n = 1
mem = deque([(1, seed)])

while seed != 1 and seed != 0:
    x = 2
    while True:
        if seed ** x > c:
            break
        x += 1
    if n * x <= b:
        seed = seed ** x % c
        n *= x
        if seed == mem[0][1]:
            break
        mem.appendleft((n, seed))
    else:
        break

rlt = 0
for i, j in mem:
    if rlt == 0:
        b -= i
        rlt = j
    if i <= b:
        rlt *= j ** (b // i)
        b %= i

rlt %= c
print(rlt)
