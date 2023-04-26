# CS 공부하면서 마주쳤던 Linked List를 여기서 만났네요

def solution(n, k, cmds):
    arr = ['O'] * n
    delStack = []  # 삭제칸 저장용 stack
    linked_list = {i: [i-1, i+1] for i in range(n)}
    linked_list[0][0] = linked_list[n-1][1] = None

    for cmd in cmds:
        # [1] C: 현재 행 삭제
        if cmd == "C":
            before, after = linked_list[k]
            arr[k] = 'X'
            delStack.append((before, k, after))

            if k == n-1: k = before  # 막행이면 앞으로~
            else: k = after          # 아니면 뒤로~

            if before == None:
                linked_list[after][0] = None
            elif after == None:
                linked_list[before][1] = None
            else:
                linked_list[after][0] = before  # 끊어내기
                linked_list[before][1] = after  # 끊어내기

        # [2] Z: 삭제 행 복구
        elif cmd == "Z":
            before, temp_k, after = delStack.pop()
            arr[temp_k] = 'O'

            if before == None:
                linked_list[after][0] = None
            elif after == None:
                linked_list[before][1] = None
            else:
                linked_list[after][0] = temp_k   # 다시 연결
                linked_list[before][1] = temp_k  # 다시 연결

        else:
            cmd, x = list(cmd.split())
            # [3] D: 아래 이동
            if cmd[0] == "D":
                for _ in range(int(x)):
                    k = linked_list[k][1]
            # [4] U: 위 이동
            elif cmd[0] == "U":
                for _ in range(int(x)):
                    k = linked_list[k][0]

    answer = ''.join(arr)
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))