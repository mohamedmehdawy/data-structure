import ctypes

class Array:
    def __init__(self, size):
        self.array_data_type = ctypes.py_object * size
        self.memory = self.array_data_type()
        self.size = size
        
        for i in range(size):
            self.memory[i] = None
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        return self.memory[idx]
    
    def __setitem__(self, idx, value):
        self.memory[idx] = value
    def append(self, item):
        # create new array
        array_data_type = ctypes.py_object * (self.size + 1)
        new_memory = array_data_type()
        
        # copy old array
        for i in range(self.size):
            new_memory[i] = self.memory[i]
            
        # put new element
        new_memory[self.size] = item
        self.size += 1
        
        # del old array
        del self.memory
        self.memory = new_memory

arr = Array(1)
arr[0] = "ahmed"
arr.append(20)
print(arr[1])