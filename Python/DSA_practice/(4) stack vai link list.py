class Node:
    def __init__(self ,item = None,next = None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self ,start=None):
        self.start = start

    def push(self,item):
        n = Node(item,self.start)
        self.start = n
       
    def pop(self,data):
        self.start = self.start.next
    def peek(self):
        temp = self.start
        print ("The peek value is ",temp.item)
    
    def print_Stack(self):
        temp = self.start
        while temp is not None:
            print (temp.item)
            temp = temp.next

    
stack = SLL()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop(3)
stack.peek()
stack.print_Stack()