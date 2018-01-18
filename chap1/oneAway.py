def oneReplace(a, b):
    replace = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if replace == False:
                replace = True
            else:
                return False
    return True

def oneMore(a, b):
    replace = False
    j = 0
    for i in range(len(a)):
        if a[i] != b[j]:
            if replace == False and a[i] == b[i+1]:
                replace = True
                j += 1
            else:
                return False
        j += 1
    return True

def oneAway(a, b):
    n = len(a)
    m = len(b)
   
    if m == n :
        return oneReplace(a, b)
    elif m == n+1 :
        return oneMore(a, b)
    elif m == n-1 :
        return oneMore(b, a)
    else:
        return False
        
a = 'more'
b = 'mare'
print a, b
print oneAway(a,b)
a = 'mare'
b = 'marce'
print a, b
print oneAway(a,b)
a = 'amore'
b = 'more'
print a, b
print oneAway(a,b)
a = 'mare'
b = 'mare'
print a, b
print oneAway(a,b)
a = 'mare'
b = 'mori'
print a, b
print oneAway(a,b)
a = 'mare'
b = 'marci'
print a, b
print oneAway(a,b)
a = 'mare'
b = 'mio'
print a, b
print oneAway(a,b)

