from graph import *
from minimalTree import minimalTree

def checkBalanced(t):
    def _checkBalanced(t):
        if not t:
            return True, 0
            
        isRightBalanced, rightHeight = _checkBalanced(t.right)
        isLeftBalanced, leftHeight = _checkBalanced(t.left)
        isBalanced = (isRightBalanced and isLeftBalanced and abs(rightHeight - leftHeight) < 2)
        height = max(rightHeight,leftHeight) + 1

        return isBalanced, height

    isBalanced, _ = _checkBalanced(t)
    return isBalanced

# example
t = minimalTree(range(1,10))
print checkBalanced(t) # True
t.left.right.right.right = Tree(11)
print checkBalanced(t) # False
