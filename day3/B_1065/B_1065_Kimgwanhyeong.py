num = int(input())
if num < 100:
    print(num)
elif num <= 1000:
    count = 99
    for i in range(100,num+1):
        first = i // 100
        second = (i // 10) % 10
        last = i % 10
        if second - first == last - second:
            count += 1
        elif first - second == second - last:
            count += 1

    print(count)