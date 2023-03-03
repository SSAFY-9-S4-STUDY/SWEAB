cases = int(input())
for x in range(1, cases + 1):
    N, K = map(int,input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=1)
    print(f'#{x} {sum(lst[:K])}')