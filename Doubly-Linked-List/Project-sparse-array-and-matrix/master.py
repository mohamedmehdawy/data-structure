import inspect
from package.sparseArray import SparseArray

class SparseMatrix:
    def __init__(self, row, column) -> None:
        
        # set row and colunm
        self.row = row
        self.column = column
        
        # set row array
        self.row_array = SparseArray(row)
        
    
    def set_value(self, row, col, value):
        """
            this function set value for the node insted of row and column
            parameters:
                row: the row of sparse matrix
                column: the column of sparse matrix
                value: the value of the node
        """
        # get current node insted of the row
        current_row = self.row_array.get_node(row)
        
        # check if have value or not
        # if not have value, set the new array for it
        
        
        if not current_row.data:
            current_row.data = SparseArray(self.column)

        # set value to the node insted of row and col
        current_row.data.set_value(col, value)
        
    def __repr__(self) -> str:
        # current row
        current_row = self.row_array.head
        
        # results
        results = []
        
        while current_row:
            results.append(f"Row {current_row.idx}: {current_row.data}")
            current_row = current_row.next
        
        return "\n".join(results)

    def print_as_2d_array(self):
        """
            this function print the sparse matrix like an array
            return: the result of printing
        """
        
        # set row results
        rows_result = []
        
        # set current
        current = self.row_array.head
        
        for i in range(self.row):
            
            if current and i == current.idx:
                # append row column
                rows_result.append(f"{current.data.print_as_array()}")
                current = current.next
            else:
                # row of zeros
                zero_row = ["0" for _ in range(self.column)]
                
                rows_result.append(" ".join(zero_row))
                
        
        return "\n".join(rows_result)

def test1(data, row, column, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => set value")
    
    ll = SparseMatrix(row, column)
    

    for ele in data:
        for row in range(1, len(ele)):
            ll.set_value(ele[0], ele[row][0], ele[row][1])
    

    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {func_name}"

def test2(data, row, column, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => print as 2d array")
    
    ll = SparseMatrix(row, column)
    

    for ele in data:
        for row in range(1, len(ele)):
            ll.set_value(ele[0], ele[row][0], ele[row][1])
    
    result = ll.print_as_2d_array()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={ll.print_as_2d_array()} in {func_name}"

if __name__ == "__main__":
    # test 1 => set value
    test1([[1,[1,5], [2,10]], [3, [1,50]]],7,7, "Row 1: 5@1, 10@2\nRow 3: 50@1")
    test1([[1, [6,-3]], [5, [2,6], [5,1]], [2, [5,8]], [3, [0,9], [3,7], [5,4]], [6, [6,-8]]], 7, 7, "Row 1: -3@6\nRow 2: 8@5\nRow 3: 9@0, 7@3, 4@5\nRow 5: 6@2, 1@5\nRow 6: -8@6")
    
    # test 2 => print as 2d array 
    test2([[1,[1,5], [2,10]], [3, [1,50]]],7,7, "0 0 0 0 0 0 0\n0 5 10 0 0 0 0\n0 0 0 0 0 0 0\n0 50 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0")

    print("all tests passed")