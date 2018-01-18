def zeroMatrix(a):
    firstRowHasZero = False
    firstColHasZero = False
    
    for j in range(len(a[0])):
        if a[0][j] == 0 :
            firstRowHasZero = True
            break
    
    for i in range(len(a)):
        if a[i][0] == 0 :
            firstColHasZero = True
            break
   
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0 :
                a[0][j] = 0
                a[i][0] = 0
    
    for i in range(1,len(a)):            
        for j in range(1,len(a[0])):
            if a[i][0] * a[0][j] == 0 :
                a[i][j] = 0       
    
    if firstRowHasZero :
        for j in range(len(a[0])):
            a[0][j] = 0       
            
    if firstColHasZero :
        for i in range(len(a)):
            a[i][0] = 0
