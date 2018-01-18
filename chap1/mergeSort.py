def mergeSort(a):
    aux = [0 for _ in range(len(a))]
    _mergeSort(a,aux,0,len(a)-1)

def _mergeSort(a,aux,low,high):
    mid = (low + high) / 2
    if low < high:
        _mergeSort(a,aux,low,mid)
        _mergeSort(a,aux,mid+1,high)
        merge(a,aux,low,mid,high)

def merge(a,aux,low,mid,high):
    aux[low:high+1] = a[low:high+1]
    
    left = low
    right = mid + 1
    current = low
    
    while left <= mid and right <= high:
        if aux[left] <= aux[right] :
            a[current] = aux[left]
            left += 1
        else:
            a[current] = aux[right]
            right += 1
        current += 1
        
    for i in range(mid-left+1):
        a[current+i] = aux[left+i]
        
a = [3,4,7,1,2,7,3,4,7,2,0,4,2,6,9,0]
print a
mergeSort(a)
print a
