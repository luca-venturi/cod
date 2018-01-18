from graph import *

def minimalTree(a):
    if a == []:
        return None

    i = (len(a) - 1) / 2
    return Tree(a[i],minimalTree(a[:i]),minimalTree(a[i+1:]))
    
# example
if __name__ == "__main__":
    t = minimalTree([1,2,3,4,5,6,7])
    print t.right.left.key # = 5
