# http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html

class Tree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Node:
    def __init__(self,key):
        self.key = key
        self.neighbors = {}
    
    def addNeighbor(self,nbr,weight=0):
        self.neighbors[nbr] = weight
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.nVertices = 0
    
    def addVertex(self,key):
        v = Node(key)
        self.vertices[key] = v
        
    def addEdge(self,keys,weight=0):
        self.vertices[keys[0]].neighbors[self.vertices[keys[1]]] = weight
        
    def __iter__(self):
        return iter(self.vertices.values())

def buildGraph(n,edges):
    g = Graph()
    for i in range(n): g.addVertex(i)
    for e in edges: g.addEdge(e)
    
    return g
