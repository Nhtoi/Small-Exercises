class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree():
    def __init__(self, root = None):
        self.root = root

    def CreateTree(self, root, value):
        if root.left is None:
            root.left = Node(value)
        elif root.right is None:
            root.right = Node(value)
        else:
            self.CreateTree(root.left, value)
        return root

    def Insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.CreateTree(self.root, value)
        
   
    def PrintTree(self, root):
        if root is None:
            return
        print(root.value)
        self.PrintTree(root.left)
        self.PrintTree(root.right)


tree = Tree()
tree.Insert(2)
tree.Insert(3)
tree.Insert(4)
tree.Insert(5)
tree.Insert(6)
tree.PrintTree(tree.root)

        

        