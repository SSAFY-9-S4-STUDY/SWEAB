T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    if len(Ai) < len(Bj): # Ai 가 더 길게 
        Ai, Bj = Bj, Ai
    
    max_fin = 0
    for i in range(len(Ai)-len(Bj)+1):
        temp = 0
        for k in range(len(Bj)):
            temp += Bj[k] * Ai[k+i]
        if max_fin < temp:
            max_fin = temp

    print(f'#{tc} {max_fin}')