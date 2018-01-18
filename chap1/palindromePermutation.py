def charNumber(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1

def palindromePermutation(phrase):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = charNumber(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1
    
a = 'coat cot'
print palindromePermutation(a)    
a = 'coat cet'
print palindromePermutation(a)
