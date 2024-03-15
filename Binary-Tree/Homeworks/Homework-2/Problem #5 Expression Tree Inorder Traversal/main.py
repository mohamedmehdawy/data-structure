class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, expression) -> None:
        # init root
        self.root = None
        
        # length will start with 1, because we already add the root node
        self.length = 1
        
        # operators
        self.operators = ["*", "/", "+", "-", "^"]

        # create tree insted of expression
        self.build_expression_tree_v2(expression)
        
    def is_operator(self, char):
        """
            this function check if the operator is operator or not
            parameters:
                char: the character will be check
            returns: status if the operator is operator or not
        """
        # if the char in operators return true
        if char in self.operators:
            return True
        
        # if not operator, return false
        return False
    def build_expression_tree(self, expression):
        """
            this function take the postfix expression and build a tree insted of it
            parameters:
                expression: the expression the tree will be build insted of it
        """
        # init last root
        last_root = None
        
        # loop throw the exporession in reverse way
        for index in range(len(expression)-1, -1, -1):
            # init current element and increase the length
            current_element = Node(expression[index])
            self.length += 1
            # if no root, set root and last root
            if not self.root:
                self.root = current_element
                last_root = self.root
                continue
            
            # if last root dont have right, add current element to right, else add in left
            if not last_root.right:
                last_root.right = current_element
            else:
                last_root.left = current_element
            
            # if current is operator, set last root
            if self.is_operator(current_element.data):
                last_root = current_element
    def build_expression_tree_v2(self, expression):
        """
            this function take the postfix expression and build a tree insted of it
            parameters:
                expression: the expression the tree will be build insted of it
        """
        # init nodes stack 
        nodes_stack = []
        
        # loop into each character in the expression
        for char in expression:
            # init current node
            node = Node(char)
            # if char is operator, link it with elements in the stack
            if self.is_operator(char):
                node.right = nodes_stack[-1]
                node.left = nodes_stack[-2]
                nodes_stack.pop()
                nodes_stack.pop()
            
            # append current node to the stack
            nodes_stack.append(node)
        
        # here we should have only 1 element in the stack
        assert len(nodes_stack) == 1
        
        # set the root
        self.root = nodes_stack[-1]
    def add(self, nodes, directions):
        """
            this function add nodes to the binary insted of his directions
            parameters:
                nodes: the nodes will added to the binary
                directions: the direction of the nodes
        """
        # init current
        current = self.root
        # loop insted of the index
        for index in range(len(nodes)):
            current = self.add_node(current, nodes[index], directions[index])

    def add_node(self, current, value, direction):
        """
            this function link the node insted of his direction
            parameters:
                current: the current node will linked with the target node
                value: the value of current or new node
                direction: the direction of the linked (left or right)
        """
        # increase the length
        # if the direction is left
        if direction == "L":
            if not current.left:
                # create new node and link with current.left
                current.left = Node(value)
                self.length += 1

            else:
                assert current.left.data == value
                self.length += 1

            return current.left

        # if the direction is right
        if not current.right:
            # create new node and link with current.right
            current.right = Node(value)
        else:
            assert current.right.data == value
        return current.right

    def print_inorder(self):
        """
            this function print the tree in inorder way
        """
        def inorder(current):
            """
                this function print the tree starts from the current
                parameters:
                    current: the starts root point
            """
            # if arrive to the last of the sub tree stop the recursion
            if not current:
                return

            # call for left side
            inorder(current.left)

            # print the current node
            print(current.data, end="")

            # call for right side
            inorder(current.right)
        inorder(self.root)
        print()

    def first_not_perfect_check(self):
        """
            this function handle first check for the tree if no have any node or 1 node
            returns:
                true if the tree is not perfect
        """
        return self.length <= 1
    def _tree_height(self, root):
        """
            this function return the height of the sub tree
            parameters:
                root: the root you will start get the height from it
                height: the height of the subtree
            returns: the height of the sub tree
        """
        # if no root, return -1
        if not root:
            return -1
        
        # return the max of left and right
        return 1 + max(self._tree_height(root.left), self._tree_height(root.right))
    
    def tree_height(self):
        """
            this function return the height of the tree
            returns: the height of the tree
        """
        return self._tree_height(self.root)
    def _tree_nodes(self, current):
        """
            this function return the total number of nodes
            parameters:
                current: the current node
            returns: total number of tree nodes
        """
        # if no current return 0
        if not current:
            return 0
        
        return 1 + self._tree_nodes(current.left) + self._tree_nodes(current.right)
    def tree_nodes(self):
        """
            this function return the total number of nodes
            returns: total number of tree nodes
        """
        
        return self._tree_nodes(self.root)
    
    def print_inorder_expression(self):
        """
            this function print the tree indorder with handle paranthese
        """
        def inorder(current):
            """
                this function walk throw the tree in print it with paranthese
                parameters:
                    current: the current node
            """
            
            # if leaf, reutn current data
            if not current.left and not current.right:
                return current.data
            
            # get data of left side and right side
            left_side = inorder(current.left)
            right_side = inorder(current.right)
            
            # if the current is not root, return it with paranthese, else return with out
            if current is not self.root:
                return f"({left_side}{current.data}{right_side})"

            return f"{left_side}{current.data}{right_side}"

        print(inorder(self.root))
if __name__ == "__main__":
    tree = BinaryTree("23+4*")
    
    tree.print_inorder()
    tree.print_inorder_expression()
    
    tree2 = BinaryTree("51+2/")
    
    tree2.print_inorder()
    tree2.print_inorder_expression()
    
    tree3 = BinaryTree("534*2^+")
    
    tree3.print_inorder()
    tree3.print_inorder_expression()
    