C = int(input())
for s in range(C):
    
    N = list(map(int, input().split()))
        
    avg = sum(N[1:]) / N[0]

    avg_up = 0
    for i in N[1:]:
        if avg < i:
            avg_up += 1
    rlt = round(avg_up / N[0] * 100, 3)
    print(f"{rlt:.3f}%")