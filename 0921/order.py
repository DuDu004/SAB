
n=7
tree = [0, 2, 4, 6, 7, 1, 5, 8]
def preorder(now):
    if now <= n:
        print(tree[now], end=" ")
        preorder(now*2)
        preorder(now*2 + 1)

preorder(1)


def inoreder(num1):
    if now <= n:
        inorder(num1*2)
        print(tree[num], end=" ")
        inorder(num1*2 + 1)

inorder(1)


def postorder(num2):
    print(tree[num], end=" ")
    postorder(num2)
    postorder(num2*2 -1)

postorder(1)