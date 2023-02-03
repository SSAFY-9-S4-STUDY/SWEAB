import sys
N = int(sys.stdin.readline())

words = [sys.stdin.readline().replace('\n','') for i in range(N)]
words.sort(key = lambda x:(len(x),x))

for i in words:
    print(i)