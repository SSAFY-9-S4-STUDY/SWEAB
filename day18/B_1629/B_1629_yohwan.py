import sys
A, B, C = map(int,sys.stdin.readline().split())

def remain(B):
    if B == 1:
        return A % C
    if B % 2 == 0:
        return remain(B//2) ** 2 % C
    if B % 2 == 1:
        return A * remain(B//2) ** 2 % C
    
print(remain(B))

# 머리 깨지고있었는데 힌트준 조장님 감사,,,

