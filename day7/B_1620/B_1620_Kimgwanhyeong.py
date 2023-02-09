N, M = map(int, input().split())
dic = [0 for _ in range(N+1)]
for idx in range(1,N+1):
    dic[idx] = input()

for _ in range(M):
    sch = input()
    rst = 0
    if sch.isdigit():
        rst = dic[int(sch)]
    elif sch.isalpha():
        for idx in range(N+1):
            if dic[idx] == sch:
                rst = idx
    print(rst)