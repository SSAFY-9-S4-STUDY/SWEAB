# 원래 함수 안에서 pre += parent[node_idx] 대신 print(parent[node_idx], end='')로 바로 출력했는데
# 뒤에 None이 붙어서 출력되더라구요..? 디버깅 돌려봐도 이유를 모르겠어서
# 변수 만들고 거기 계속 더해준 다음에 함수 실행하고 pre, in_, post 출력했네요..
# 깔끔하게 정리는 못했습니당ㅠ

def preorder(node_idx):
    global pre
    pre += parent[node_idx]
    if left[node_idx]:
        preorder(ord(left[node_idx])-65)
    if right[node_idx]:
        preorder(ord(right[node_idx])-65)


def inorder(node_idx):
    global in_
    if left[node_idx]:
        inorder(ord(left[node_idx])-65)
    in_ += parent[node_idx]
    if right[node_idx]:
        inorder(ord(right[node_idx])-65)


def postorder(node_idx):
    global post
    if left[node_idx]:
        postorder(ord(left[node_idx])-65)
    if right[node_idx]:
        postorder(ord(right[node_idx])-65)
    post += parent[node_idx]


N = int(input())

parent = list(map(chr, range(65, 65 + N)))
left = [0] * N
right = [0] * N

for _ in range(N):
    p, l, r = input().split()

    idx = parent.index(p)
    if l != '.':
        left[idx] = l
    if r != '.':
        right[idx] = r

pre = in_ = post = ''

preorder(0)
inorder(0)
postorder(0)

print(pre)
print(in_)
print(post)