def zero_num_in_N_fac(N):
    cnt_list = [0,0] # N 에 2가 곱해진 횟수, 5가 곱해진 횟수
    N1 = N
    N2 = N
    while N1 // 2 > 0: # N 에 2 가 곱해진 갯수를 알아냄
        cnt_list[0] += N1 // 2
        N1 /= 2
    while N2 // 5 > 0:
        cnt_list[1] += N2 // 5
        N2 /= 5
    return cnt_list

N, M = map(int,input().split())
k1 = zero_num_in_N_fac(N)
k2 = zero_num_in_N_fac(M)
k3 = zero_num_in_N_fac(N-M)
a = min([k1[0]-k2[0]-k3[0], k1[1]-k2[1]-k3[1]])

print(int(a))
