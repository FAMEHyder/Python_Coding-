class Node:
    def __init__(self):
        self.item = []
    def is_emoty(self):
        if len(self.item==0):
            return None
    def inser_at_last(self,data):
        self.item.append(data)
    def delete_first(self):
        self.item.pop(0)
    
    def insert_first(self,data):
        index = 0;
        element = data
        self.item.insert(index,element)
    
    def delete_last(self):
        self.item[-1]
        self.item.pop()
        

n1 = Node()
n1.insert_first(1)
n1.insert_first(1)
n1.inser_at_last(2)
n1.inser_at_last(2)
n1.delete_first()
n1.delete_last()

print (n1.item)