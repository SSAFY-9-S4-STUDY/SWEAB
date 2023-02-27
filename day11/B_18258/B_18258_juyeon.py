from collections import deque
def queue_jy(arr:list):
    global q
    global idx, res
    if len(arr) == 2:
        q.append(arr[1])
    elif arr[0] == 'pop':
        idx += 1
        if q:
            res[idx] = q.popleft()
        else:
            res[idx] = -1
    elif arr[0] == 'size':
        idx += 1
        res[idx] = len(q)
    elif arr[0] == 'empty':
        idx += 1
        res[idx] = 0 + (q == deque([]))
    elif arr[0] == 'front':
        idx += 1
        if q:
            res[idx] = q[0]
        else:
            res[idx] = -1

    elif arr[0] == 'back':
        idx += 1
        if q:
            res[idx] = q[-1]
        else:
            res[idx] = -1

N = int(input())
res = [None]*N
idx = -1

q = deque([])
for tc in range(N):
    word = input().split()
    queue_jy(word)
    # print(q)
for l in range(idx+1):
    print(res[l])