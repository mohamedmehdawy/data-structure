import ctypes

class Array:
    def __init__(self, size):
        self._capacity = max(16, size * 2) # actual memory size
        self.size = size # user size
        
        # create array
        self.array_data_type = ctypes.py_object * self._capacity
        self.memory = self.array_data_type()
        
        for i in range(self._capacity):
            self.memory[i] = None
        

    def expend_capacity(self):
        # set new value to capacity
        self._capacity *= 2
        print(f"expend capacity: {self._capacity}")
        
        # create new array
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()
        
        # copy old data
        for i in range(self.size):
            new_memory[i] = self.memory[i]
        
        # delete old memory
        del self.memory
        self.memory = new_memory
    
    def append(self, item):
        # check if size arrive to capacity
        if self._capacity == self.size:
            self.expend_capacity()
        
        # set item
        self.memory[self.size] = item
        self.size += 1
    
    def insert(self, idx, item):
        if type(idx) != int:
            raise Exception("you should enter valid index")
        
        if (self.size * -1) > idx or idx >= self.size:
            raise Exception("out of range")
        
        # convert to real index if is less than 0
        if idx < 0:
            idx = self.size + idx
            
        # check if size arrive to capacity
        if self._capacity == self.size:
            self.expend_capacity()
            
        current = self.size - 1
        
        while current >= idx:
            self.memory[current + 1] = self.memory[current]
            current -= 1
        
        self.memory[idx] = item
        self.size += 1
        
    # magic methods
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        return self.memory[idx]
    
    def __setitem__(self, idx, value):
        self.memory[idx] = value
    
    def __repr__(self) -> str:
        result = '['
        for i in range(self.size):
            result += f"{self.memory[i]}{', ' if i != self.size - 1 else ''}"
        result += ']'
        return result
    