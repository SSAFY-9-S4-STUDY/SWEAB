trial = int(input())

for i in range(0, trial) :
    answers = input()
    total = 0
    score = 0
    for j in range(0, len(answers)):
        if answers[j] == 'X':
            score = 0
        if answers[j] == 'O':
            if answers[j-1] == False or answers[j-1] == 'X':
                score = 1
                total = total + score
            if answers[j-1] == 'O':
                score += 1
                total = total + score
    print(total)