t = int(input())
for test_case in range(1,t+1):
    num, *scores = map(int,input().split())
    avg = sum(scores) // num
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    
    rst = round(float(count * 100 / num),3)
    
    print(str(rst)+'%')