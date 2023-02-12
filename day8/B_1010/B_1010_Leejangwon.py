import sys
from math import comb

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(comb(m, n))
