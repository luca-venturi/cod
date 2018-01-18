def isPermutation(a, b):
    d = [0 for _ in range(128)]
    for x in a:
        d[ord(x)] += 1
    for x in b:
        d[ord(x)] -= 1
    for x in d:
        if x != 0:
            return False
    return True
    
a = 'abbello'
b = 'allebbo'
print a, b
print isPermutation(a, b)

a = 'abbe llo'
b = 'alleppo'
print a, b
print isPermutation(a, b)
