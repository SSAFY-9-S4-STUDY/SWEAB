def ishannum(x):    
    result = 1
    if x > 99:
        lst_l = list(map(int,list(str(x)))) 
        for i in range(len(lst_l)-2):
            if lst_l[i]-lst_l[i+1] == lst_l[i+1]-lst_l[i+2]:                
                continue 
            else: result = 0

    return result

N = int(input())
han_num = 0
for n in range(1, N+1):
    han_num += ishannum(n)

print(han_num)