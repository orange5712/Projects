class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def createNode(key):
    return Node(key)

def displayTree(root, space):
    if root is None:
        return
    
    space += 10

    displayTree(root.right, space)

    print()
    for _ in range(10, space):
        print(" ", end="")
    print(root.key)

    displayTree(root.left, space)

def max(a, b):
    return a if a > b else b

def makeheight(n):
    if n is None:
        return 0
    else:
        n.height = 1 + max(makeheight(n.left), makeheight(n.right))
        return n.height

def getHeight(n):
    return n.height if n else 0

def getBalanceFactor(n):
    if n is None:
        return 0
    return getHeight(n.left) - getHeight(n.right)

def Search(G, k):
    if G is None:
        return None
    if k == G.key:
        return G
    if k < G.key:
        return Search(G.left, k)
    if k > G.key:
        return Search(G.right, k)

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    x.height = max(getHeight(x.right), getHeight(x.left)) + 1
    y.height = max(getHeight(y.right), getHeight(y.left)) + 1

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(getHeight(x.right), getHeight(x.left)) + 1
    y.height = max(getHeight(y.right), getHeight(y.left)) + 1

    return y

def insert(node, key):
    if node is None:
        return createNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    bf = getBalanceFactor(node)

    if bf > 1 and key < node.left.key:
        return rightRotate(node)

    if bf < -1 and key > node.right.key:
        return leftRotate(node)

    if bf > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    if bf < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def preOrder(root):
    if root:
        print(f"({root.key},{getBalanceFactor(root)})", end=" ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(f"({root.key},{getBalanceFactor(root)})", end=" ")
        inOrder(root.right)

def delete_node(node, key):
    if node is None:
        return node

    if key < node.key:
        node.left = delete_node(node.left, key)
    elif key > node.key:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.key = temp.key
        node.right = delete_node(node.right, temp.key)

    if node is None:
        return node

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalanceFactor(node)

    if balance > 1 and getBalanceFactor(node.left) >= 0:
        return rightRotate(node)

    if balance < -1 and getBalanceFactor(node.right) <= 0:
        return leftRotate(node)

    if balance > 1 and getBalanceFactor(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    if balance < -1 and getBalanceFactor(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def Balance(node):
    makeheight(node)
    if node is None:
        return node

    bf = getBalanceFactor(node)

    if bf > 1:
        if node.left.left is not None:
            return rightRotate(node)
        node.left = leftRotate(node.left)
        return rightRotate(node)
    elif bf < -1:
        if node.right.right is not None:
            return leftRotate(node)
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    if node.left:
        node.left = Balance(node.left)
    if node.right:
        node.right = Balance(node.right)
    
    return node

def check(G):
    if G is None:
        return 0
    if abs(getBalanceFactor(G)) > 1:
        return 1
    return check(G.left) or check(G.right)

def Delete(root, k):
    delete_node(root, k)
    while check(root):
        root = Balance(root)
    return root

if __name__ == "__main__":
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 60)
    root = insert(root, 70)
    root = insert(root, 80)
    root = insert(root, 90)
    root = insert(root, 100)

    root = Delete(root, 80)
 
 

    makeheight(root)
    preOrder(root)
    print()
    inOrder(root)
    print()
    displayTree(root, 10)
