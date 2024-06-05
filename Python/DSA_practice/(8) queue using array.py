from array import*
class queue:
    def __init__(self):
        self.item =array ('i',[])

    def is_empty(self):
        return len(self.item)==0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        print ("dequeuing the  element : ")
        if not self.is_empty():
            
            return self.item.pop(0)
        else :
            print ("Queue underflow")
    def get_front(self):
        if not self.is_empty():
            print ("The front value is : ")
            return self.item [0]

    def get_rear(self):
        if not self.is_empty():
            print ("The rear value is : ")
            return self.item[-1]
        
    def size_of_queue(self):
        print ("The size of queue is now : ")
        return len(self.item)
    def print_queue(self):
        print (self.item)



Que = queue()
Que.enqueue(1)
Que.enqueue(2)
Que.enqueue(3)
Que.enqueue(4)
Que.enqueue(5)
print (Que.get_front())
print (Que.get_rear())
print (Que.size_of_queue())
print (Que.dequeue())
print (Que.dequeue())
