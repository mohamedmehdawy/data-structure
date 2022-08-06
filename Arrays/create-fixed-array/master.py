import ctypes

class Array:
    def __init__(self, size):
        self.array_of_types = ctypes.py_object * size
        self.memory = self.array_of_types()
        self.size = size
        
        for i in range(size):
            self.memory[i] = None
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        return self.memory[idx]
    
    def __setitem__(self, idx, value):
        self.memory[idx] = value
