import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

def counttwo(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n
    return cnt

def countfive(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

ans = min(countfive(n) - countfive(m) - countfive(n - m), counttwo(n) - counttwo(m) - counttwo(n - m))
print(ans)