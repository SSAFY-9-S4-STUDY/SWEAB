# 시간 부족으로 최적화는 못함,, 코드 더 줄일 수 있는 방안 있을듯 초안에 풀고 검토토 못함 ㅜ_ㅜ 



import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(st, end):
    if st > end:
        return 
    # mid = st
    mid = end
    for k in range(st, end+1):
        if tree[k] > tree[st]:
            mid = k-1
            break
    
    postorder(st+1, mid)
    postorder(mid+1, end)
    res.append(tree[st])

res = []
postorder(0, len(tree)-1)
for i in res:
    print(i)