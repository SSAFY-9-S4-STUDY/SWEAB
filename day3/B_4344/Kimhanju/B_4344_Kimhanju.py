import sys

C = int(sys.stdin.readline())

for _ in range(C):
    N,*scores = list(map(int,sys.stdin.readline().split()))
    over_mean = list(filter(lambda x: x>sum(scores)/N,scores))
    print("%0.3f%%" %(len(over_mean)/len(scores)*100))