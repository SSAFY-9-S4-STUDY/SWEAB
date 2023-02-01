import sys
sys.stdin = open('input.txt','r')

def count_k(row,k):
    remove_zero = ''.join(row).split('0')
    return remove_zero.count('1'*K)

T = int(input())

for test_case in range(1,T+1):

    N, K = map(int,input().split())

    spaces_origin = []

    for _ in range(N):
        spaces_origin.append(input().split())

    spaces_transpose = zip(*spaces_origin)

    answer = 0

    for i,j in zip(spaces_origin,spaces_transpose):
        answer = answer + count_k(i,K) + count_k(j,K)

    print(f'#{test_case} {answer}')
