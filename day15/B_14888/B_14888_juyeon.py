cal_dict = {
    0:lambda x, y : x + y,
    1:lambda x, y : x - y,
    2:lambda x, y : x * y,
    3:lambda x, y : int(x / y)
}

def DFS(num_list):
    global cal, res, min_res, max_res
    if len(num_list) == 1:
        if num_list[0] <= min_res:
            min_res = num_list[0]
        if num_list[0] >= max_res:
            max_res = num_list[0]
        return
    
    for idx in range(4):
        if cal[idx]:
            cal[idx] -= 1
            x, y = num_list.pop(0), num_list.pop(0)
            res = cal_dict[idx](x, y)
            DFS([res]+num_list)
            cal[idx] += 1
            res -= cal_dict[idx](x, y)
            num_list = [x, y] + num_list
        

N = int(input())
num_list = list(map(int,input().split()))
cal = list(map(int,input().split()))

min_res = 10**22
max_res = -10**22
res = 0
DFS(num_list)
print(max_res)
print(min_res)