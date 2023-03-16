# 전위 순회한 결과(num_lst)를 arguments에 넣어서
# 후위 순회하는 함수 post_order를 정의
def post_order(num_lst):
    # 숫자 리스트의 길이가 1이거나 0이면 그 리스트 그대로 반환함.
    if len(num_lst) <= 1:
        return num_lst

    # 전위 순회한 결과 리스트의 0번째 인덱스 값이 서브 트리의 루트 노드의 값.
    # 그 값보다 크다면 루트 노드의 오른쪽 자식 노드들이므로
    # i 번째의 바로 직전 까지의 리스트가 왼쪽 자식 노드들.
    # 후위 순회(post_order) 의 순서에 따라 L - R - V
    for i in range(1,len(num_lst)):
        if num_lst[i] > num_lst[0]:
            return post_order(num_lst[1:i]) + post_order(num_lst[i:]) + [num_lst[0]]

    
    return post_order(num_lst[1:]) + [num_lst[0]]


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
num_lst = []
while True:
    try:
        num = int(input())
        num_lst.append(num)
    except:
        break

ans = post_order(num_lst)
for i in ans:
    print(i)