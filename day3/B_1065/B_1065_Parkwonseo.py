N = int(input())

def hansu (num):
    list_hansu = []
    checkpoint = 0
    for i in str(num):
        list_hansu.append(int(i))
    for i in range(1, len(list_hansu) - 1):
        if list_hansu[i] - list_hansu[i - 1] == list_hansu[i + 1] - list_hansu[i]:
            checkpoint += 1
    if checkpoint == len(list_hansu) - 2:
        return 1
    else:
        return 0
    
rlt = 99
if N >= 100:
    for i in range(100, N + 1):
        rlt += hansu(i)
    print(rlt)
else:
    rlt = N
    print(rlt)