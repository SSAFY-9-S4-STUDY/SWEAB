import sys
from math import comb

n, k = map(int, sys.stdin.readline().rstrip().split())

ans = comb(n, k) % 10007
print(ans)