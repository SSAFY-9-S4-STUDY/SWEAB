def dotting(N):
    
    if N == 3:
        return ['***', '* *', '***']
        

    else:
        K = N // 3
        past = dotting(K)
        line_1 = [past[i]*3 for i in range(K)]   # ['*********', '* ** ** *', '*********']

        line_2 = []
        for i in range(K):
            line_2.append(past[i]+ ' '*K + past[i])

        return [*line_1, *line_2, *line_1]
        

N = int(input())
for i in dotting(N):
    print(i)