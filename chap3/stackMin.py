from stack import stack

class stackMin:
    def __init__(self):
        self.values = []
        
    def pop(self):
        self.values.pop()
        
    def push(self,value):
        self.values.append((value,min(value,self.min))
        
    def peek(self):
        return self.values[-1][0]
    
    def min(self):
        return self.values[-1][1]
        
    def isEmpty(self):
        return len(self.values) == 0
        
class stackMin2():
    self.s1 = stack()
    self.s2 = stack()
    
    def pop(self):
        self.s1.pop()
        
    
        
    
