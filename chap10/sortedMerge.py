def sortedMerge(a,b,indexA,indexB):
    indexA -= 1
    indexB -= 1
    total = indexB + indexA + 1
    
    while indexB >= 0:
        if b[indexB] >= a[indexA]:
            a[total] = b[indexB]
            indexB -= 1
        else:
            a[total] = a[indexA]
            indexA -= 1
        total -= 1

a = [1,3,5,7,None,None,None]
b = [2,4,6]
print a, b
sortedMerge(a,b,4,3) 
print a
