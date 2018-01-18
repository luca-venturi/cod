def quickSort(a):
    _quickSort(a, 0, a.size)
    
def _quickSort(a, left, right):
    index = partition(a, left, right)
    if left < index - 1 :
        _quickSort(a, left, index - 1)
    if index < right :
        _quickSort(a, index, right)

def partition:
    
    
