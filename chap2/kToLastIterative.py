class linkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
def kToLastIterative(ll,k):
    p0 = ll
    p1 = ll
    for i in range(k+1):
        if p1 == None :
            print 'list has less than', k+1, 'elements'
            return linkedList()
        p1 = p1.next
    while p1 != None :
        p0 = p0.next
        p1 = p1.next
    return p0
    
ll = linkedList(2,linkedList(3,linkedList(0,linkedList(1))))
print kToLastIterative(ll,0).value
print kToLastIterative(ll,1).value
print kToLastIterative(ll,2).value
print kToLastIterative(ll,3).value
print kToLastIterative(ll,4).value
ll = linkedList(1)
print kToLastIterative(ll,0).value
print kToLastIterative(ll,1).value
ll = None
print kToLastIterative(ll,0).value
