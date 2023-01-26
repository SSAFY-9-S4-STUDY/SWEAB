n = int(input())

for i in range(n):
    score = 0
    count = 0
    result_list = list(input())

    for j in range(len(result_list)):
        if result_list[j] == 'X':
            count = 0
        else:
            count += 1
        score = score + count
    
    print(score)