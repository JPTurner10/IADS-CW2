import math
import copy


# DO NOT EDIT AdjNode
class AdjNode:
    def __init__(self,value):
        self.node = value
        self.next = None

class Graph:
    # DO NOT EDIT
    # Basic initialisation where we don't have file input.
    def __init__(self, num):
        self.n = num
        self.weights = [None] * self.n
        self.graph = [None] * self.n
        self.degs = [0] * self.n

    # Initialisation where we got the graph input from a file,
    # might be weighted or unweighted.  It is your responsibility
    # to complete this method as your work for Part B.
    def __init__(self,num,filename,weighted):
        if num > 0:
            self.n = num
            self.weights = [1] * self.n
            self.graph = [None] * self.n
            self.degs = [0] * self.n
            reader = open(filename,'r')
            lines = reader.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].split()
            if weighted:
                for i in range(0, num):
                    self.weights[i] = int(lines[i][1])
                for i in range(num+1, len(lines)):
                    self.add_edge(int(lines[i][0]), int(lines[i][1]))
            else:
                for line in lines:
                    self.add_edge(int(line[0]), int(line[1]))

            
    # DO NOT EDIT
    # This is a given method to assist with buiding the Adjacency
    # list structure.  
    def add_edge(self, u, v):
        self.degs[u] += 1
        self.degs[v] += 1
        Adju = self.graph[u]
        vNode = AdjNode(v)
        vNode.next = Adju
        self.graph[u] = vNode
        Adjv = self.graph[v]
        uNode = AdjNode(u)
        uNode.next = Adjv
        self.graph[v] = uNode

    # DO NOT EDIT
    # A given method of possible value for your implementations.
    def del_edge(self, u, v):
        curr = self.graph[u]
        if curr and curr.node == v:
            self.graph[u] = curr.next
            self.degs[u] -= 1
        else:
            while curr.next and (curr.next).node != v:
                curr = curr.next
            if curr.next:
                nextnext = (curr.next).next
                curr.next = nextnext
                self.degs[u] -= 1
        curr = self.graph[v]
        if curr	and curr.node == u:
            self.graph[v] = curr.next
            self.degs[v] -= 1
        else:
            while curr.next and (curr.next).node != u:
                curr = curr.next
            if curr.next:
                nextnext = (curr.next).next
                curr.next = nextnext
                self.degs[v] -= 1      
                           
    # DO NOT EDIT
    # This method can be used to display the Adjacency list structure
    # to assist in debugging 
    def print_out_graph(self):
        for i in range(self.n):
            print("Vertex " + str(i) + "(weight " + str(self.weights[i]) + "):", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.node), end="")
                temp = temp.next
            print(" \n")

    # It is your responsibility to complete this method as your
    # work for Part C.  You should work with criterion (a) for
    # this implementation, covering both weighted and unweighted
    # cases (weighted being modelled with ``all 1s" in self.weights
    def GreedyIS(self):
        inIS = [0] * self.n
        deg = (self.degs).copy()
        fresh = copy.deepcopy(self.graph)
        while 0 in inIS:
            u = self.arga(inIS, deg)
            inIS[u] = 1
            neighbours = self.Nbd(u, fresh) 
            for w in neighbours:
                inIS[w] = -1
                for i in range(0, self.n-1):
                    neighbours = self.Nbd(i, fresh)
                    if w in neighbours:
                        self.del_edge_new(i, w, fresh, deg)
        for i in range(self.n):
            inIS[i] = max(0, inIS[i])
        return inIS

    # It is your responsibility to complete this method as your
    # work for Part C.  You should work with criterion (b) for                 
    # this implementation.
    def GreedyIS_b(self):
        inIS = [0] * self.n
        deg = (self.degs).copy()
        fresh = copy.deepcopy(self.graph)
        while 0 in inIS:
            u = self.argb(inIS)
            inIS[u] = 1
            neighbours = self.Nbd(u, fresh) 
            for w in neighbours:
                inIS[w] = -1
                for i in range(0, self.n-1):
                    neighbours = self.Nbd(i, fresh)
                    if w in neighbours:
                        self.del_edge_new(i, w, fresh, deg)
        for i in range(self.n):
            inIS[i] = max(0, inIS[i])
        return inIS
    
    def arga(self, inIS, deg):
        max_value = -1
        max_index = -1
        for i in range(0, self.n):
            if inIS[i] == 0:
                if deg[i] == 0:
                    return i
                else:
                    temp = (self.weights[i] / deg[i])
                    if temp > max_value:
                        max_value = temp
                        max_index = i
        return max_index
    
    def argb(self, inIS):
        max_value = -1
        max_index = -1
        for i in range(self.n):
            if inIS[i] == 0:
                if self.weights[i] > max_value:
                    max_value = self.weights[i]
                    max_index = i
        return max_index
    
    def Nbd(self, u, fresh):
        neighbours = []
        temp = fresh[u]
        while temp != None:
            neighbours.append(temp.node)
            temp = temp.next
        return neighbours
    

    def del_edge_new(self, u, v, fresh, deg):
        curr = fresh[u]
        if curr and curr.node == v:
            fresh[u] = curr.next
            deg[u] -= 1
        else:
            while curr.next and (curr.next).node != v:
                curr = curr.next
            if curr.next:
                nextnext = (curr.next).next
                curr.next = nextnext
                deg[u] -= 1
        curr = fresh[v]
        if curr	and curr.node == u:
            fresh[v] = curr.next
            deg[v] -= 1
        else:
            while curr.next and (curr.next).node != u:
                curr = curr.next
            if curr.next:
                nextnext = (curr.next).next
                curr.next = nextnext
                deg[v] -= 1




gU = Graph(7, "graph1U", False)
IS = gU.GreedyIS()
print(IS)
gW = Graph(7, "graph1W", True)
IS = gW.GreedyIS()
print(IS)
gU = Graph(7, "graph1U", False)
IS = gU.GreedyIS_b()
print(IS)
gW = Graph(7, "graph1W", True)
IS = gW.GreedyIS_b()
print(IS)


