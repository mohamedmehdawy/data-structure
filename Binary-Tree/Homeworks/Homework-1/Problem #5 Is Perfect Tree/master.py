class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)
        # length will start with 1, because we already add the root node
        self.length = 1

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
        print("")
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
    
    def inorder_iterative(self):
        """
            this function print the tree inorder using iterative way
        """
        # init the stack and push the root to him
        # each element in the stack will be: [node, show number]
        stack = [[self.root, 0]]
        
        # iterative until the stack is empty
        while stack:
            # get last node from the stack
            current_node_data = stack[len(stack) - 1]
            
            # if the current node is none remove from the stack and continue
            if not current_node_data[0]:
                stack.pop()
                continue
            
            # if not have left and right, print it and remove from the stack
            if not current_node_data[0].left and not current_node_data[0].right:
                print(current_node_data[0].data, end="")
                stack.pop()
                continue
            # increase show by 1
            current_node_data[1] += 1
            
            # if the show is 1, append left
            if current_node_data[1] == 1:
                stack.append([current_node_data[0].left, 0])
            # if the show is 1, append right
            elif current_node_data[1] == 2:
                print(current_node_data[0].data, end="")
                stack.append([current_node_data[0].right, 0])
            # here mean i call the left and right and this time to remove the current node
            else:
                stack.pop()
        print("")

    def inorder_iterative_v2(self):
        """
            this function return the tree inorder using iterative way
            returns: the tree inorder using iterative way
        """
        # init stack with result
        stack = []
        result = []
        
        # append root to the stack
        stack.append([self.root, False])
        
        while stack:
            # get current node with his flag
            current_node, is_completed = stack[len(stack) - 1]
            
            # remove current node from the stack
            stack.pop()
            
            # if current node is completed, append it to result
            if is_completed:
                result.append(current_node)
            else:
                # check right first because we need the left check first in the stack
                # we need left be the last one to be the first one in the check
                if current_node.right:
                    stack.append([current_node.right, False])
                
                # append current with flag true because we end it
                stack.append([current_node, True])
                
                if current_node.left:
                    stack.append([current_node.left, False])
        return result
def print_tree(root):
    """
        this function the binary tree recursively
        parameters:
            root: the root will start print the left and right from it
    """
    # if the root is none, return none(stop recursive)
    if not root:
        return None

    # print the data
    print(root.data)

    # call the function for subtress
    print_tree(root.left)

    print_tree(root.right)


def print_expression(root):
    """
        this funciton print the binary as postfix
        parameters:
            root: the root will start print the left and right from it
    """
    # check if the root is operator
    if not str(root.data).isdigit():
        left_side = print_expression(root.left)
        right_side = print_expression(root.right)

        return f"{left_side}{right_side}{root.data}"

    # if the root is a number, just return the value
    return root.data


def print_expression_postfix(root):
    """
        this funciton print the binary as postfix
        parameters:
            root: the root will start print the left and right from it
    """
    # if not have a root, the parent is a number
    if not root:
        return
    print_expression_postfix(root.left)
    print_expression_postfix(root.right)

    print(root.data, end='')


if __name__ == "__main__":

    # tree
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ["L", "L", "L",])
    tree.add([2, 4, 8], ["L", "L", "R",])
    tree.add([2, 5, 9], ["L", "R", "R",])
    tree.add([3, 6, 10], ["R", "R", "L",])

    tree.print_inorder()
    tree.inorder_iterative()
    print(tree.inorder_iterative_v2())
    # # create 8 nodes
    # root = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(6)
    # node7 = Node(7)
    # node8 = Node(8)

    # # link them together

    # root.left = node2
    # root.right = node3

    # node2.left = node4
    # node2.right = node5

    # node5.right = node7

    # node3.right = node6

    # node6.left = node8

    # print_tree(root)

    # tree = BinaryTree()
    # tree.root = root
    # tree.print_inorder()
    # # test for print expression
    # root = Node("*")

    # node2 = Node("+")
    # node3 = Node(4)

    # node4 = Node(2)
    # node5 = Node(3)

    # # link nodes

    # root.left = node2
    # root.right = node3

    # node2.left = node4
    # node2.right = node5

    # print(print_expression(root))
    # print_expression_postfix(root)
