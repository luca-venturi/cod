from linkedList import printLinkedList

class linkedList :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
        
def removeDups(ll):
    prev = None
    seen = {}
    while ll :
        if not seen.get(ll.value, False):
            seen[ll.value] = 1
            prev = ll
        else:
            prev.next = ll.next
        ll = ll.next
            
ll = linkedList(3,linkedList(4,linkedList(5,linkedList(4,linkedList(6,)))))
printLinkedList(ll)
removeDups(ll)
printLinkedList(ll)

def removeDupsNoBuffer(ll):
    current = ll
    while current :
        runner = current
        while runner.next :
            if runner.next.value == current.value :
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        
ll = linkedList(3,linkedList(4,linkedList(5,linkedList(4,linkedList(6,)))))
printLinkedList(ll)
removeDupsNoBuffer(ll)
printLinkedList(ll)
