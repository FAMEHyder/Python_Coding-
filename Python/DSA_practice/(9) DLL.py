class Node:
    def __init__(self, prev = None,item =None,next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_first(self,item):
        n = Node(None,item,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self,item):
        temp = self.start
        
        while temp.next is not None:

            temp = temp.next
        n = Node(temp,item,None)
        temp.next = n

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item ==data:
                return temp
            temp = temp.next

        
        return None
        
    def inser_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n


    def print_list(self):
        temp = self.start

        while temp is not None:
            
            # print (temp.prev)
            print (temp.item , end ='  ')
            # print (temp.next)
            temp = temp.next

    def delete_first(self):

        if self.start.next is not None:
            self.start = self.start.next
            self.start.prev = None
        else:
            self.start = None
    def delete_last(self):
        temp = self.start
        if self.start.next is None:
                self.start = None
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.item==data:
                self.start = None
        else:
            temp = self.start
            while temp is not None:
                if temp.item ==data:
                    if temp.next is not None:
                        temp.next.prev =temp.next
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next


        


list = DLL()
list.insert_at_first(4)
list.insert_at_first(3)
list.insert_at_first(2)
list.insert_at_first(1)
list.insert_at_last(6)
list.inser_after(list.search(4),5)
list.delete_first()
list.delete_first()
list.delete_first()
# list.delete_first()
# list.delete_first()
# list.delete_last()
# list.delete_last()
# list.delete_last()
list.delete_item(4)
list.delete_item(5)
list.is_empty()
list.print_list()
