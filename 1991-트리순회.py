'''
<input>
1st --> 이진 트리의 노드 개수 n
2nd~ --> n개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어짐

<output>
1st --> 전위순회
2nd --> 중위순회
3rd --> 후위순회
'''

n = int(input()) ## 노드의 개수
binary_tree = {}

for _ in range(n):
    node, left, right = input().split()
    binary_tree[node] = [left, right]


def pre_Order(node):
    if node == '.':
        return

    print(node, end="")
    pre_Order(binary_tree[node][0])
    pre_Order(binary_tree[node][1])


def in_Order(node):
    if node == '.':
        return

    in_Order(binary_tree[node][0])
    print(node, end="")
    in_Order(binary_tree[node][1])


def post_Order(node):
    if node == '.':
        return

    post_Order(binary_tree[node][0])
    post_Order(binary_tree[node][1])
    print(node, end="")


pre_Order('A')
print()
in_Order('A')
print()
post_Order('A')