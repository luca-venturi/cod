def groupAnagrams(a):
    h = {}
    for x in a:
        tmp = ''.join(sorted(x))
        if not h.get(tmp, False):
            h[tmp] = [x,]
        else:
            h[tmp].append(x)
    i = 0
    for b in h.values():
        for x in b:
            a[i] = x
            i += 1

a = ['uno','essere','onu','eresse']
print a
groupAnagrams(a)
print a 
