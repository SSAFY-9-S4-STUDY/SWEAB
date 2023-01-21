trial = int(input())

for i in range(0, trial) :
    student_test = list(map(int, input().split()))
    over_average = []
    average = sum(student_test[1:len(student_test)]) / student_test[0]
    print(average)
    for j in student_test[1:len(student_test)]:
        if j > average:
            over_average.append(j)
    print(f'{round(len(over_average) / student_test[0] * 100, 3)}%')