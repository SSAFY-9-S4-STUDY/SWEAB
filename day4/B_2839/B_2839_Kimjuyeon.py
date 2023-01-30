salt = int(input())

box_5 = salt // 5
min_x = salt
for i in range(box_5 + 1):
    box_3 = (salt - 5 * i) / 3
    if int(box_3) != box_3: 
        continue
    
    if min_x <= i+box_3:
        continue
    
    min_x = int(i+box_3)


print(min_x if min_x != salt else -1)