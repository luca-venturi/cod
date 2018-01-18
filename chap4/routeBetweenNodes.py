from graph import *
from Queue import Queue

def routeBetweenNodes(g,key1,key2):
    start = g.vertices[key1]
    end = g.vertices[key2]
    
    visited = {v:False for v in g}
    q = Queue()
    visited[start] = True
    q.put(start)
    
    while not q.empty():
        v = q.get()
        for n in v.neighbors:
            if not visited[n]:
                visited[n] = True
                q.put(n)
                
    return visited[end]

# test cases

g = buildGraph(4,[[0,1],[1,2]])
print routeBetweenNodes(g,0,2)
g = buildGraph(4,[[0,1],[2,3]])
print routeBetweenNodes(g,0,2)
