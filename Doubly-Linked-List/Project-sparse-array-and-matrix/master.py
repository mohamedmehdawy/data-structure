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
    
    
    def add(self, second):
        """
            this function add the second sparse matrix to the first one
            parameters:
                second: the second matrix
        """
        # check first if have the same row and column
        if not (self.row == second.row and self.column == second.column):
            print("the two sparse matrix dont have the same row and column")
            return
        
        # set current start from the first element in second
        second_current = second.row_array.head
        
        while second_current:
            # get the node of first matrix
            row_node = self.row_array.get_node(second_current.idx)
            
            # if not have any data, set the same data of second current
            if not row_node.data:
                row_node.data = SparseArray(self.column)
            
            
            row_node.data.add(second_current.data)
            second_current = second_current.next
    def __getitem__(self, indexs):
        """
            this this function get the row of the sparse matrix
        """
        # check first the idx of row
        row_node = self.row_array[indexs[0]]
        if not (row_node and row_node.data):
            return None
        
        # get the column node
        column_node = row_node.data[indexs[1]]
        
        return column_node
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

def test3(data, row, column, second_data, second_row, second_column, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => add")
    
    first = SparseMatrix(row, column)
    

    for ele in data:
        for row in range(1, len(ele)):
            first.set_value(ele[0], ele[row][0], ele[row][1])
    
    second = SparseMatrix(second_row, second_column)
    
    for ele in second_data:
        for row in range(1, len(ele)):
            second.set_value(ele[0], ele[row][0], ele[row][1])
    
    first.add(second)
    
    result = str(first)
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"


def test4(data, row, column, idx_row, idx_column, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => get item")
    
    ll = SparseMatrix(row, column)
    

    for ele in data:
        for row in range(1, len(ele)):
            ll.set_value(ele[0], ele[row][0], ele[row][1])
    
    
    result = ll[idx_row, idx_column]
    
    
    assert str(result) == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"

if __name__ == "__main__":
    # test 1 => set value
    test1([[1,[1,5], [2,10]], [3, [1,50]]],7,7, "Row 1: 5@1, 10@2\nRow 3: 50@1")
    test1([[1, [6,-3]], [5, [2,6], [5,1]], [2, [5,8]], [3, [0,9], [3,7], [5,4]], [6, [6,-8]]], 7, 7, "Row 1: -3@6\nRow 2: 8@5\nRow 3: 9@0, 7@3, 4@5\nRow 5: 6@2, 1@5\nRow 6: -8@6")
    
    # test 2 => print as 2d array 
    test2([[1,[1,5], [2,10]], [3, [1,50]]],7,7, "0 0 0 0 0 0 0\n0 5 10 0 0 0 0\n0 0 0 0 0 0 0\n0 50 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0")

    # test 3 => add
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [], 7,7, "Row 1: 5@1, 10@2\nRow 3: 50@1")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [[2, [1,5]]], 1,7, "Row 1: 5@1, 10@2\nRow 3: 50@1")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [], 7,2, "Row 1: 5@1, 10@2\nRow 3: 50@1")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [[1, [1,6]]], 7,7, "Row 1: 11@1, 10@2\nRow 3: 50@1")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [[1, [1,6]], [6, [1,20], [5, 50]]], 7,7, "Row 1: 11@1, 10@2\nRow 3: 50@1\nRow 6: 20@1, 50@5")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [[1, [1,6]], [6, [1,20], [5, 50]], [5, [4, 30]]], 7,7, "Row 1: 11@1, 10@2\nRow 3: 50@1\nRow 5: 30@4\nRow 6: 20@1, 50@5")
    test3([[1,[1,5], [2,10]], [3, [1,50]]],7,7, [[1, [1,6], [3, 100], [2,12]], [6, [1,20], [5, 50]], [5, [4, 30]]], 7,7, "Row 1: 11@1, 22@2, 100@3\nRow 3: 50@1\nRow 5: 30@4\nRow 6: 20@1, 50@5")

    # test 4 => get item
    test4([[1,[1,5], [2,10]], [3, [1,50]]], 7, 7, 1, 1, "5@1")
    test4([[1,[1,5], [2,10]], [3, [1,50]]], 7, 7, 1, 3, "None")
    
    print("all tests passed")