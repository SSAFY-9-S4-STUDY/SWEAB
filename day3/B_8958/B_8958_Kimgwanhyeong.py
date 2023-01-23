t = int(input())
for test_case in range(1,t+1):
    ox = list(input())
    count = 0
    cumul_score = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cumul_score += 1
            count += cumul_score
        else:
            cumul_score = 0

    print(count)