import sys
sys.setrecursionlimit(10**9)

def tree(S, E):
    if S > E:
        return

    idx = E + 1

    for i in range(S+1, E+1):
        if lst[S] < lst[i]:
            idx = i
            break

    tree(S+1, idx-1)
    tree(idx, E)
    print(lst[S])


lst = []
count = 0

while count <= 10000:
    try:
        N = int(input())
    except:
        break
    lst.append(N)
    count += 1

tree(0, len(lst)-1)