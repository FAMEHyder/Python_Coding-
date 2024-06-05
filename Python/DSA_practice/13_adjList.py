class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjList={ v:[] for v in range(vertex) }
    def addEdge(self,u,v,weight=1):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            self.adjList[u].append((v,weight))
            self.adjList[v].append((u,weight))

    def remEdge(self,u,v):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            self.adjList[u]=[(v,weight) for vertex , weight in self.adjList[u] if vertex != v]
            self.adjList[v]=[(u,weight) for vertex , weight in self.adjList[v] if vertex != u]
    
    def hasedge(self,u,v):
        if 0<=u<self.vertex and 0<=v<self.vertex:
            return any(vertex==v for vertex, x in self.adjList[u])
        else:
            print('invalid vertex')

    def printEdge(self):
        for vertex,n in self.adjList.items():
            print(vertex,"-->",n)

obj1=Graph(5)
obj1.addEdge(0,1)
obj1.addEdge(0,2)
obj1.addEdge(1,3)
obj1.addEdge(2,3)
obj1.addEdge(2,4)
obj1.printEdge()
obj1.remEdge(1,1)
print ("Printing edge after removing edge")
print(obj1.hasedge(10,3))
obj1.printEdge()