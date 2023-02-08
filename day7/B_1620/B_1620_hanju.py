import sys

N, M = map(int,sys.stdin.readline().split())

guide_int = [0]*(N+1)
guide_str = dict()

for i in range(1,N+1):
    pokemon = sys.stdin.readline()[:-1]
    guide_str[pokemon] = i
    guide_int[i] = pokemon

for i in range(M):
    tmp = sys.stdin.readline()[:-1]
    try:
        print(guide_int[int(tmp)])
    except:
        print(guide_str[tmp])
