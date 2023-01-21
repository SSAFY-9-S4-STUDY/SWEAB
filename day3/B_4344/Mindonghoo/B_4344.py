trial = int(input())

for i in range(0, trial) :
    stest = list(map(int, input().split()))
    over_average = []
    average = sum(stest[1:len(stest)]) / stest[0]
    print(average)
    for j in stest[1:len(stest)]:
        if j > average:
            over_average.append(j)
    print("{:.3f}%".format(round(len(over_average) / stest[0] * 100, 3)))