'''stack: 
        last in first out '''

class stack:
    def __init__(self):

        self.item = []

    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            print ("underflow")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            print ("list is empty")

    def print_stack(self):
        if self.is_empty():
           print ("stack is empty")
        else :
            print ("stack")
            for item in reversed(self.item):
                print (item)



s1=stack()
s2=stack()

s2.push(1)
s2.push(2)
s2.push(3)
s2.print_stack()
print ("Top element of s2 is :",s2.peek())
print ("Pop element of s2 is :",s2.pop())
print ("Top element of s2 is :",s2.peek())
s2.print_stack()

print ("for s1")
print ("Top element of s1 is ",s1.peek())