def _get(a, i):
    try:
        x = a[i]
        return x 
    except IndexError:
        return -1

def sortedSearchNoSize(a, x):
    low = 0
    if _get(a, low) == -1:
        return -1
    high = 1    
    while _get(a, high) != -1:
         high *= 2
    while low < high:
        mid = (low + high) / 2
        tmp = _get(a, mid)
        if tmp == -1 or tmp > x:
            high = mid
        elif tmp < x:
            low = mid
        else:
            return mid
    return -1        
                  
a = [2,3,4,5,6,7]
print a
print sortedSearchNoSize(a, 5)
print sortedSearchNoSize(a, 1)
