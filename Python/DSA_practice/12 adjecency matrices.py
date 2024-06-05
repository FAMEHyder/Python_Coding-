class graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.ad_matrix = [ [0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.ad_matrix[u][v]=weight
            self.ad_matrix[v][u]=weight
        else:
            print ("Invalid vertex")

    def remove_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            self.ad_matrix[u][v]=0
            self.ad_matrix[v][u]=0

        else:
            print ("Invalid vertex")
    def has_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            return self.ad_matrix[u][v]!=0
        else:
            print ("Invalid vertex")

    def print_ad_matrix(self):
        for row_list in self.ad_matrix:
            print (" ".join(map(str,row_list)))


g = graph(5)
g.add_edge(0,1)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(4,3)
g.print_ad_matrix()