class queue:
    def __init__(self , maxsize):
        self.first = 0 
        self.last = 0
        self.maxsize = maxsize
        self.arr = [None]*(maxsize + 1)
    
    def isEmpty(self):
        if(self.first == self.last):
            return 1
        else:
            return 0
    
    def isFull(self):
        if((self.last + 1)%(self.maxsize + 1) == self.first):
            return 1
        else:
            return 0
    
    def put(self , num):
        if(not self.isFull()):
            self.last = (self.last + 1)%(self.maxsize + 1)
            self.arr[self.last] = num
    
    def get(self):
        if(not self.isEmpty()):
            self.first = (self.first + 1)%(self.maxsize + 1)
            return self.arr[self.first]

if __name__ == "__main__":
    q1 = queue(5)
    i = 0
    while(not q1.isFull()):
        q1.put(i)
        i = i + 1
            
    