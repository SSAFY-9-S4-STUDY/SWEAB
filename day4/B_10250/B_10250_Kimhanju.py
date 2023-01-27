import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    stage= str(N % H) if N%H != 0 else str(H) 
    room = str((N) // H + 1) if N%H != 0 else str((N) // H)
    print(stage+room.zfill(2))
