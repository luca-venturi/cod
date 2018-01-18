class heap:
    def __init__(self):
        self.values = []
        self.len = 0
        
    def percUp(self,i):
        while (i+1) // 2 > 0:
            if self.values[i] < self.values[(i-1)//2]:
                tmp = self.values[(i-1)//2]
                self.values[(i-1)//2] = self.values[i]
                self.values[i] = tmp
            i = (i-1)// 2
    
    def put(self,value):
        self.values.append(value)
        self.len += 1
        self.percUp(self.len-1)
        
    def minChild(self,i):
        if i*2+1 == self.len-1:
            return i*2+1
        else:
            if self.values[i*2+1] < self.values[(i+1)*2]:
                return i*2+1
            else:
                return (i+1)*2
        
    def percDown(self,i):
        while i*2 < self.len-1:
            mc = self.minChild(i)
            if self.values[i] > self.values[mc]:
                tmp = self.values[i]
                self.values[i] = self.values[mc]
                self.values[mc] = tmp
            i = mc
        
    def get(self):
        _min = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.len -= 1
        self.percDown(0)
        
        return _min

    def make(self,l):
        self.values = l[:]
        self.len = len(l)
            
        i = self.len // 2 - 1
        while i >= 0:
            self.percDown(i)
            i -= 1
            
if __name__ == '__main__':
    h = heap()
    h.make(list(range(8))[::-1])
    
    for i in range(8):
        print(h.get())
