class Node:
    def __init__(self ,left,item,right):
        self.left = left
        self.item = item
        self.right = right

class Tree:
    def __init__(self,root  = None):
        self.root = root
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert (self,root,data):
        if root is None:
            return Node(None,data,None)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)


t1 = Tree()
t1.insert(100)
t1.insert(80)
t1.insert(90)
t1.insert(120)
print (t1.inorder())
print (t1.preorder())
print (t1.postorder())