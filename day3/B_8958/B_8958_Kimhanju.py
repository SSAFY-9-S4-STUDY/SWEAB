import sys

T = int(sys.stdin.readline())

for i in range(T):

    answer = 0

    for i in sys.stdin.readline().split('X'):
        cnt = i.count('O')
        answer += cnt*(cnt+1)//2
        
    print(answer)

