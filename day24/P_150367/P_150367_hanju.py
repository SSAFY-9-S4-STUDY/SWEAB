from collections import deque

def solution(numbers):
    res = []
    # 결과를 구한 숫자를 저장할 딕셔너리
    possible_dic = dict()
    # 숫자 배열을 돌면서 결과 구하기
    for num in numbers:
        # 이미 결과를 구한 숫자면 딕셔너리에서 결과를 갖고옴
        previous = possible_dic.get(num)
        if previous == 0 or previous == 1:
            res.append(previous)
            continue
        # 총 노드 개수 구하기
        bin_num = bin(num)[2:]
        total_nod, tmp_nod = 1, len(bin_num)
        while tmp_nod > total_nod:
            total_nod = total_nod*2 + 1
        # 총 노드에 부족한 수 만큼 0(빈 노드) 채우기
        bin_num = '0'*(total_nod-tmp_nod) + bin_num
        # 이진트리를 돌며 가능한지 탐색
        queue = deque([(bin_num, total_nod)])
        while queue:
            total, N = queue.popleft()
            # 노드가 한 개라면 무조건 존재 가능
            if N == 1:
                continue
            # 중앙노드, 왼쪽 트리, 오른쪽 트리
            N //= 2
            center, left_tree, right_tree = total[N], total[:N], total[N+1:]
            # 중앙 노드가 존재하지 않는데 왼쪽 or 오른쪽 트리에 노드가 존재할 수 없음
            # 노드가 유효하지 않다면 결과 배열에 2 추가
            if center=='0' and (left_tree.count('1') or right_tree.count('1')):
                possible_dic[num] = 0
                res.append(0)
                break
            # 현재 상태가 유효하다면 큐에 왼쪽 트리, 오른쪽 트리를 추가
            queue.append((left_tree,N))
            queue.append((right_tree,N))
        # 모든 노드가 유효하다면 결과 배열에 1 추가
        else:
            possible_dic[num] = 1
            res.append(1)

    return res

print(solution([63, 111, 95]))

            

            
