num = int(input())
count = 0
check = num

while True:
    sum = num//10 + num%10
    sum_next = num%10 * 10 + sum%10
    
    count += 1
    num = sum_next
    
    if sum_next == check:
        break
        
print(count)