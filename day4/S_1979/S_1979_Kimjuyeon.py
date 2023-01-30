def word_num(lst):
    word_lst = []
    for i in lst: 
        a = ''.join(i)
        temp_lst = a.split('0') 
        word_lst.append(temp_lst)
    return word_lst


T = int(input())
for i in range(T):
    N, K = map(int,input().split())
    num_K = '1'*K
    
    puzzle_ori = []
    for j in range(N):
        puzzle_ori.append(list(map(str,input().split())))
    
    puzzle_rev = list(zip(*puzzle_ori))

    cnt = 0
    for j in sum(word_num(puzzle_ori),[]):
        if num_K == j: 
            cnt += 1
        else: pass
    for j in sum(word_num(puzzle_rev),[]):
        if num_K == j: 
            cnt += 1
        else: pass            

    print(f'#{i+1} {cnt}')