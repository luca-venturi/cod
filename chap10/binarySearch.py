def binarySearch(a, x):
    low = 0
    high = a.size - 1
    
    while low <= high :
        mid = ( low + high ) / 2
        if a[mid] < x :
            low = mid + 1
        elif a[mid] > x :
            high = mid - 1
        else :
            return mid
    
    return -1
    
def recursiveBinarySearch(a, x, low, high):
    if low > high :
        return -1
    
    mid = ( low + high )  / 2 
    if a[mid] < x :
        return recursiveBinarySearch(a, x, mid + 1, high)
    elif a[mid] > x :
        return recursiveBinarySearch(a, x, low, mid - 1)
    else:
        return mid
