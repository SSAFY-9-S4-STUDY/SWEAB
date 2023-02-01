def decimal_list(n):
    numbers = [1,1,]+[0]*(n-1) #[1,1,0,0,0,0,0,0,0,] 인덱스: 0, 1, 2, 3, ... n

    for idx in range(2, int(n ** 0.5)+1):
        if numbers[idx] == 0:
            for num in range(idx+1,n+1):
                if numbers[num] == 0:
                    if not (num) % idx:
                        numbers[num] = 1
    return numbers


st, end = map(int,input().split())

numbers_list = decimal_list(end)

for i in range(st,end+1):
    if numbers_list[i]==0:
        print(i)
        
        
