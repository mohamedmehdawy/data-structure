class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

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
    # create 8 nodes
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    # link them together

    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    node5.right = node7

    node3.right = node6

    node6.left = node8

    print_tree(root)

    tree = BinaryTree()
    tree.root = root
    tree.print_inorder()
    # test for print expression
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
