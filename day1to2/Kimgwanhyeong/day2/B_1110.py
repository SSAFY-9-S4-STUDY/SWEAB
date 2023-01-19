num = int(input())
count = 1
spare, rem = divmod(num, 10)
spare, rem = rem, (spare + rem)%10
while spare*10+rem != num:
    spare, rem = rem, (spare + rem)%10
    count +=1
print(count)