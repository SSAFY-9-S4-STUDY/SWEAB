T = int(input())
array = [[0]*100 for i in range(100)]
# print(array)

for test_case in range(1, T+1):
    x, y = map(int, input().split())
    count = 0

    for j in range(x, x+10):
        for k in range(y, y+10):
            array[j][k] = 1
    
    for row in array:
        count += row.count(1)
        
print(count)