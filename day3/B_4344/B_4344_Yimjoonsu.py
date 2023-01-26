n = int(input())

for i in range(n):
    stu_overavg = 0
    score_list = list(map(int, input().split(' ')))
    score_only = score_list[1:]
    average = sum(score_only)/score_list[0]
    
    for j in range(len(score_only)):
        if score_only[j] > average:
            stu_overavg += 1
        result = stu_overavg/len(score_only) * 100
    print(f'{result:.3f}%')