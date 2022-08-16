import sys
sys.path.append("d:\\My-Work\\python\\data strucure\\Arrays")
from fixedArray import Array

class Array2D:
    def __init__(self, row, column, init_value = 0):
        self.row = row
        self.column = column
        self.memory = Array(row)
        
        for i in range(row):
            self.memory[i] = Array(column)
        
        for i in range(row):
            for j in range(column):
                self.memory[i][j] = init_value
    def two_operation_check(self, target):
        if type(self) != type(target):
            raise Exception("unsupported type")
        
        if self.row != target.row or self.column != target.column:
            raise Exception("row and column must be same in objects")
    def __add__(self, target):
        
        self.two_operation_check(target)
        result = Array2D(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result[i][j] = self[i][j] + target[i][j]
        return result

    def __mul__(self, target):
        self.two_operation_check(target)
        result = Array2D(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result[i][j] = self[i][j] * target[i][j]
        return result
    def __getitem__(self, idx):
        return self.memory[idx]

    def __repr__(self) -> str:
        result = "["
        for i in range(self.row):
            result += "["
            for j in range(self.column):
                result += f"{self.memory[i][j]}{', ' if j != self.column - 1 else ''}"
            result += "]"
        result += "]"
        return result
    
if __name__ == "__main__":
    array = Array2D(2, 4)
    array2 = Array2D(2, 4)
    array[0][2] = 3
    array[1][1] = 5
    array[1][3] = 7
    array2[0][2] = 2
    array2[1][1] = 10
    array2[1][3] = 3
    print(array * array2)

    # print(array)
    # print(array)
    # print(array[1][3])



