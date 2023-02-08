n, m = map(int, input().split())

poket = []
for i in range(n):
    poket.append(input())

search = []

for i in range(m):
    search.append(input())
    # try:
    #     search[i] = int(search[i])
    # except:
    #     continue

for i in search:
    # if type(i) == int:
    #     print(poket[i - 1])
    if 48 <= ord(i[0]) <= 57:
        print(poket[int(i) - 1])    
    elif type(i) == str:
        print(poket.index(i) + 1)

# 주석된 것들로 하니 시간초과.
# 아무래도 try except가 시간을 많이 잡아먹는 것 같음.
# 대입되는 데이터가 많은것 같을땐 입력 받으면서 조건을 추가하는 것 보다,
# 입력 된 후에 필요한 데이터를 찾는 곳에서 시간을 쓰는게 맞는 것 같다.
# 아니면 한주가 알려준 방법(input 말고 sys로 받기)을 한번 이용해 보는 것도 좋을 것 같다.