def solution(numbers):
    N = len(numbers)
    answer = [1] * N

    def tree_check(tree, idx):
        # [1] 이미 이진트리로 표현할 수 없다고 판별났을 때
        if answer[idx] == 0 or len(tree) == 1:
            return
        # [2] 검사: 부모노드가 0이고, 자식노드 둘 다 1이면 X
        parent = len(tree) // 2
        child1, child2 = parent//2, parent + parent//2 + 1
        if tree[parent] == '0':
            if tree[child1] == '1' and tree[child2] == '1':
                answer[idx] = 0
                return
        # [3] 검사결과 괜찮으면 부모노드(루트) 기준 좌우로 또 검색
        tree_check(tree[:parent], idx)
        tree_check(tree[parent+1:], idx)


    for idx in range(N):
        # 2진수로 변환
        bin_num = bin(numbers[idx])[2:]
        # 2진수 숫자의 길이가 짝수면 맨앞에 더미노드 더해주기
        if not len(bin_num) % 2:
            bin_num = '0' + bin_num
        print(bin_num)
        # 검사 시작
        tree_check(bin_num, idx)

    return answer


print(solution([7, 42, 5, 2134]))
print(solution([63, 111, 95]))