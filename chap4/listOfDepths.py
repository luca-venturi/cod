from graph import *
from minimalTree import minimalTree
from Queue import Queue

class LinkedList:
    def __init__(self,key,next=None):
        self.key = key
        self.next = next

def listOfDepths(t):
    d = []
    q = Queue()
    q.put(t)
    
    while not q.empty():
        p = Queue()
        l = None
        while not q.empty():
            v = q.get()
            tmp = LinkedList(v.key)
            tmp.next = l
            l = tmp
            if v.left:
                p.put(v.left)
            if v.right:
                p.put(v.right)
        if l:
            d.append(l)
        q = p
        
    return d
    
# example
t = minimalTree(range(1,10))
d = listOfDepths(t)
print d[2].next.next.key # = 3
