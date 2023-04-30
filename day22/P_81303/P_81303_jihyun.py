def solution(n, k, cmd):
    linked = {i: [i-1, i+1] for i in range(n)}
    linked[0][0] = n-1
    linked[n-1][1] = 0
    
    del_lst = []
    for info in cmd:                
        if info == "C":            
            pre, nxt = linked[k]
            linked[pre][1] = nxt
            linked[nxt][0] = pre
            
            del_lst.append([k, linked[k]])
            del linked[k]
            
            if nxt < k:
                k = pre
            else:
                k = nxt
                
        elif info == "Z":
            res, val = del_lst.pop()
            linked[res] = val
            pre, nxt = val
            linked[pre][1] = res
            linked[nxt][0] = res
            
        else:
            st, num = info.split()
            num = int(num)
            if st == "U":
                for _ in range(num):
                    k = linked[k][0]

            else:
                for _ in range(num):
                    k = linked[k][1]
            
    answer = ""
    for idx in range(n):
        if idx in linked:
            answer += "O"
        else:
            answer += "X"
    return answer