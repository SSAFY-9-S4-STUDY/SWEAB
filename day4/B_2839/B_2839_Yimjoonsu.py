n = int(input())
count = 0

while(n>0):
    if n == 1 or n == 2 :
        n = -1
        count = -1
    elif n % 5 == 0:
        count += n//5
        break
    else:
        n -= 3
        count += 1
print(count)