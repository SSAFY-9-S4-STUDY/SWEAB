k = int(input()) # 참외개수
M, x = map(int,input().split())
N, y = map(int,input().split())
area = x * y

for _ in range(2):
    M_in, x_in = map(int,input().split())
    N_in, y_in = map(int,input().split())
    if M_in == M:
        x += x_in
    else:
        x -= x_in
    
    y1 = -y_in if N_in != N else y_in
    
    area += x * y1


print(abs(area)*k)