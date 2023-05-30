class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None: 
        return Node(key)
    else:
        if(root.data == key):
            return root
        elif(root.data < key):
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
def leftRotate(root, key):
    if(root is None):
        return root
    if(root.data == key):
        newRoot = root.right 
        root.right = newRoot.left
        newRoot.left = root
        return newRoot
    elif(root.data < key):
        root.right = leftRotate(root.right, key)
    else:
        root.left = leftRotate(root.left, key)
    return root


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
inorder(r)
print("After left rotation")
r = leftRotate(r, 30)
inorder(r)