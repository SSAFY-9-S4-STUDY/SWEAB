T = int(input())
for i in range(T):
    M, *scores = map(int, input().split())
    ave = sum(scores) / len(scores)
    
    best_student = [J for J in scores if J > ave]
    
    print(f'{round((len(best_student) / M)*100,3):.3f}%')
    