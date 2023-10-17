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
            results.append(f"ROW {current_row.idx}: {current_row.data}")
            current_row = current_row.next
        
        return "\n".join(results)


def test1(row, column, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => set value")
    
    ll = SparseMatrix(row, column)
    

    ll.set_value(1,1,5)
    ll.set_value(1,2,10)

    print(f"the value is: {ll}")
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {func_name}"



if __name__ == "__main__":
    test1(7,7, "ROW 1: 5@1, 10@2")
    
    print("all tests passed")