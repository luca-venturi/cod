class linkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
class doublyLinkedList:
    def __init__(self, value=None, next=None, prev=None):  
        self.value = value
        self.next = next
        self.prev = prev
        
def printLinkedList(ll):
    _list = []
    while ll:
        _list.append(ll.value)
        ll = ll.next
    print _list
