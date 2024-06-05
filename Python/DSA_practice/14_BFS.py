from collections import deque
class mygraph:
    def __init__(self,a):
        self.vertex_count = a
        self.adj_list = { v: [] for v in range(a)}

    def add(self,u,v):
        if 0 <= u <self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list [u].append(v)
            self.adj_list [v].append(u)
        else:
            print("Invalid vertex")

    def print_adj_list(self):
        for v , n in self.adj_list.items():
            print (v,':',n)
    
    def bfs(self,start):
        if 0<= start < self.vertex_count:
            visited = set()
            queue= deque([start])
            visited .add(start)
            while queue:
                vertex = queue.popleft()
                print (vertex,end=' ')
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.qppend (neighbor)
                    visited.add(neighbor)
        else:
            print ("starting vertex is not valid")
t = mygraph(11)
t.add(1,2)
t.add(1,4)
t.add(4,3)
t.add(3,10)
t.add(3,9)
t.add(2,5)
t.add(2,7)
t.add(2,8)
t.add(5,8)
t.add(5,7)
t.add(5,6)
t.add(8,7)
print ("Addjecency list")
t.print_adj_list()
vertex_num = 1
print ("\n BFS traversal from vertex ",vertex_num,":")
t.bfs(vertex_num)