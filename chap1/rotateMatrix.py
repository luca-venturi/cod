# assuming non-empty square matrix

def rotateMatrix(a):
    n = len(a)
    for layer in range(n/2):
        first = layer
        last = n - first - 1
        for i in range(last - first):
            tmp = a[first][first+i]
            a[first][first+i] = a[last-i][first]
            a[last-i][first] = a[last][last-i]
            a[last][last-i] = a[first+i][last]
            a[first+i][last] = tmp
