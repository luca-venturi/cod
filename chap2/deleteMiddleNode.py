from linkedList import printLinkedList

class linkedList :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
        
def deleteMiddleNode(v):
    while v and v.next :
        v.value = v.next.value
        v.next = v.next.next
    
ll = linkedList(3,linkedList(4,linkedList(5,linkedList(4,linkedList(6,)))))
printLinkedList(ll)
deleteMiddleNode(ll.next.next)
printLinkedList(ll)

