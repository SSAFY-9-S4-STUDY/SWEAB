def promising(arr, x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x]- arr[i]) == x - i:
            return False
    return True

def bfs(x):
    global result 
    
    if x == N:
        result += 1

    else: 
        for i in range(1, N+1):
            arr[x] = i
            if promising(arr,x):
                bfs(x+1)

N = int(input())
arr = [0] * N
result = 0
bfs(0)
print(result)