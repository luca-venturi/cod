def isRotation(a, b):
    if len(a) == len(b) and b in (a+a) :
        return True
    return False
