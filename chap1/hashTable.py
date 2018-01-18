class hashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        _hash = self.hashFunction(key,self.size)
        
        if self.slots[_hash] == None:
            self.slots[_hash] = key
            self.data[_hash] = data
        else:
            if self.slots[_hash] == key:
                self.data[_hash] = data
        else:
            next = self.rehash(_hash,self.size)
            while self.slots[next] != None and self.slots[next] != key:
                next = self.rehash(next,self.size)

        if self.slots[next] == None:
            self.slots[next] = key
            self.data[next] = data
        else:
            self.data[next] = data
