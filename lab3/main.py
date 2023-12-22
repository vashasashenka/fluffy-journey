class BinNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

def insert_node(root, data):
    if root is None:
        return BinNode(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root

def sorted_nodes(root):
    result = []
    inorder_traversal(root, result)
    return result

def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.data, end=" ")
    print_inorder(node.right)

def construct_tree(expression):
    stack = []
    root = None
    for char in expression:
        if char == "(":
            new_node = BinNode(None)
            if root is None:
                root = new_node
            else:
                top = stack[-1]
                if top.left is None:
                    top.left = new_node
                else:
                    top.right = new_node
            stack.append(new_node)
        elif char == ")":
            stack.pop()
        else:
            if char.isdigit():
                if stack[-1].data is None:
                    stack[-1].data = int(char)
                else:
                    stack[-1].data = stack[-1].data * 10 + int(char)
    return root

expression = '(1 ((12) 3))'
tree = construct_tree(expression)
print("Вывод: ")
print_inorder(tree)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def BintoAVL(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.BintoAVL(arr[:mid])
        root.right = self.BintoAVL(arr[mid + 1:])
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = Node(key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        self._balance(node)

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.right = self._delete(min_node.key, node.right)

        if not node:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        self._balance(node)

        return node

    def _height(self, node):
        if not node:
            return 0
