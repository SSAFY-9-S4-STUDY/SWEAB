import sys
sys.stdin = open("input.txt")


sugar = int(input())
bag_3 = 0
bag_5 = 0 

# 남은 설탕이 5의 배수가 될 때까지 혹은 음수가 될 때까지
while sugar % 5 != 0 and sugar >= 0:
    sugar -= 3
    bag_3 += 1

bag_5 = sugar // 5
ans = bag_3 + bag_5

if sugar < 0:
    ans = -1
print(ans)



