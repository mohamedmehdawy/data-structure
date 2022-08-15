import ctypes


class Array:
    def __init__(self, size):
        self._capacity = max(16, size * 2)  # actual memory size
        self.size = size  # user size

        # create array
        self.array_data_type = ctypes.py_object * self._capacity
        self.memory = self.array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None
    
    def check_range(self, idx):
        """
            if index is out of the range raise error
        """
        if type(idx) != int:
            raise Exception("you should enter valid index")
        
        if  idx < (self.size * -1) or idx >= self.size:
            raise Exception("out of range")
        
        if idx < 0:
            return idx + self.size
        else:
            return idx
    
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

        idx = self.check_range(idx)

        # check if size arrive to capacity
        if self._capacity == self.size:
            self.expend_capacity()

        current = self.size - 1

        while current >= idx:
            self.memory[current + 1] = self.memory[current]
            current -= 1

        self.memory[idx] = item
        self.size += 1

    def right_rotate(self):
        current = self.memory[self.size - 1]

        for i in range(self.size - 2, -1, -1):
            self.memory[i+1] = self.memory[i]
        self.memory[0] = current

    def right_rotate_steps(self, times):
        for i in range(times % self.size):
            self.right_rotate()

    def left_rotate(self):
        current = self.memory[0]
        for i in range(1, self.size):
            self.memory[i - 1] = self.memory[i]
        self.memory[self.size - 1] = current
    
    def pop(self, idx):
        idx = self.check_range(idx)
        
        target = self.memory[idx]
        
        for i in range(idx, self.size - 1):
            self.memory[i] = self.memory[i+1]
            
        self.size -= 1
        return target
            
    def index_transposition(self, value):
        for i in range(self.size):
            if self.memory[i] == value:
                if i != 0:
                    prev = self.memory[i - 1]
                    self.memory[i - 1] = self.memory[i]
                    self.memory[i] = prev
                    return i - 1
                else:
                    return i
        return -1
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


array = Array(0)
for i in range(10, 60, 10):
    array.append(i)
    

print(array)
print(array.index_transposition(10))
print(array)
print(array.index_transposition(50))
print(array)
print(array.index_transposition(50))
print(array)
print(array.index_transposition(60))
print(array)
