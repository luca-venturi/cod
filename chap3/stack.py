class stack:
    def __init__(self):
        self.values = []
        self.min = None
    
    def pop(self):
        return self.values.pop()
        
    def push(self, value):
        self.values.append(value)
        
    def peek(self):
        return self.values[-1]
        
    def isEmpty(self):
        return self.values == []
        
    def size(self):
        return len(self.values)
