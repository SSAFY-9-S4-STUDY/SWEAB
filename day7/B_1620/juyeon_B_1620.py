N, M = map(int,input().split())
pok_dict = {}
for i in range(1, N+1):
    pok_dict[i] = input()
pok_dict_rev = {b:a for a,b in pok_dict.items()}

res = []
for _ in range(M):
    temp = input()
    if temp.isdigit():
        res.append(pok_dict[int(temp)])
    else:
        res.append(pok_dict_rev[temp])

for n in res:
    print(n)