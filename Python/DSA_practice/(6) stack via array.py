from array import*
class stack:
    def __init__(self):
        self.item = array ('i',[])

    def is_empty(self):
        if self.item ==0:
            return None

    def insert (self,data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            self.item.pop()

    def print (self):
        if self.is_empty():
            print ("Stack is empty")
        else:
            print ("your stack is ")
            for item in reversed(self.item):
                print (item)
    

stac = stack()
stac.insert(1)
stac.insert(2)
stac.insert(3)
stac.insert(4)
stac.insert(5)
stac.insert(6)
stac.insert(7)
stac.pop()
stac.pop()
stac.print()