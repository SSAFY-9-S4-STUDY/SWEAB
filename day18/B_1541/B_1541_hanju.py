nums = input().split('-')

rst = []
for i in nums:
    rst.append(sum(map(int, i.split('+'))))

print(rst[0] -sum(rst[1:]))
