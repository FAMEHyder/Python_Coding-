class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self,start=None):
        self.start = start

    def insert_at_start(self,item):
        n = Node(item,self.start)
        self.start = n

    def insert_at_last(self,item):
        n=Node(item)
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def search(self,item):
        temp = self.start
        while temp is not None:
            if temp.item==item:
                return temp
            temp = temp.next
        else:
            return None

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n        

    def print_list(self):
        temp = self.start

        while temp is not None:
            print (temp.item,end = '  ')
            temp = temp.next

    def delete_first (self):
        # if the list contain only one item
        if self.start is not None:
            self.start=self.start.next
    
    def delete_last(self):
        temp = self.start
        while temp.next.next is not  None:
            temp = temp.next
        temp.next = None

    def delete_item(self,item):
        temp = self.start
        while temp.next is not None:
            if temp.next.item==item:
                temp.next = temp.next.next
            temp = temp.next


list = SLL()
list.insert_at_start(2)
list.insert_at_start(1)
list.insert_at_last(3)
list.insert_at_last(4)
list.insert_at_last(6)
list.insert_at_last(7)
list.insert_at_last(8)
list.insert_after(list.search(4),5)
list.delete_first()
list.delete_last()
list.delete_item(3)
list.print_list()