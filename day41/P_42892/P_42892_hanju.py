from collections import deque
import sys

sys.setrecursionlimit(10**6)

def solution(nodeinfo):
	# 1. 변수 정의 및 재정의
	# 노드 개수
	N = len(nodeinfo)
	# 노드 정보에 순서 추가
	nodeinfo = [nodeinfo[i] + [i+1] for i in range(N)]
	# 노드를 y, x 기준으로 정렬
	nodeinfo.sort(key=lambda x: (-x[1], x[0]))
	# 루트 노드
	root = nodeinfo[0][2]
	if N == 1: return [[root], [root]]

	# 2. 노드간 연결 관계 표시
	# 관련 변수들
	connections = [[0,0] for _ in range(N + 1)]
	parent_nod = deque([nodeinfo[0][:] + [-1, 100001]])
	child_idx, child_level = 1, nodeinfo[1][1]
	# 탐색 진행
	while child_idx < N:
		# 부모노드의 x, y, 순서, 양쪽 끝 값
		x, y, order, left, right = parent_nod.popleft()
		# 자식 노드의 탐색
		while child_idx < N:
			c_x, c_y, c_order = nodeinfo[child_idx]
			# 노드가 현재 부모의 한계 범위에서 벗어난 경우
			if c_x < left or c_x > right or c_y != child_level: 
				child_level = c_y
				break
			# 왼쪽 자식일 경우
			if left < c_x < x: 
				connections[order][0] = c_order
				parent_nod.append((c_x, c_y, c_order, left, x))
			# 오른쪽 자식일 경우
			elif x < c_x < right: 
				connections[order][1] = c_order
				parent_nod.append((c_x, c_y, c_order, x, right))
			# 다음 자식을 탐색하기 위해서 인덱스 증가
			child_idx += 1

	# 3. 순회값 구하기
	# 전위 순회
	preorder_list = []
	def preorder(node):
		preorder_list.append(node)
		if connections[node][0]: preorder(connections[node][0])
		if connections[node][1]: preorder(connections[node][1]) 
	preorder(root)
	# 후위 순회
	postorder_list = []
	def postorder (node):
		if connections[node][0]: postorder(connections[node][0])
		if connections[node][1]: postorder(connections[node][1]) 
		postorder_list.append(node)
	postorder(root)

	return [preorder_list, postorder_list]
	


	
	

	


print(solution([[5,3]]))